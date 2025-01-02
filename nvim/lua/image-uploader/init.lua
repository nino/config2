-- WIP

local M = {}

M.config = {
  bucket_prefix = vim.env.BUCKET_URL,
  bucket_name = vim.env.BUCKET_NAME,
  b2_key_id = vim.env.B2_APPLICATION_KEY_ID,
  b2_key = vim.env.B2_APPLICATION_KEY,
  imageoptim_path = "/Applications/ImageOptim.app/Contents/MacOS/ImageOptim"
}

--- Helper function to run shell commands
--- @param cmd string
--- @return string
local function run_command(cmd)
  local output = vim.fn.system(cmd)
  if vim.v.shell_error ~= 0 then
    error(string.format("Command failed: %s", output))
  end
  return output
end

--- Scale image using ImageMagick
--- @param path string
--- @return nil
local function scale_image(path)
  local cmd = string.format("convert %s -resize 800x800> %s", path, path)
  print(cmd)
  local success, output = pcall(run_command, cmd)
  print(output)
  if not success then
    error("Image scaling failed or ImageMagick not found")
  end
end

--- Optimise images using ImageOptim
--- @param paths string[]
--- @return nil
local function optimise_images(paths)
  if #paths == 0 then
    error("No paths provided for optimisation")
  end

  local cmd = M.config.imageoptim_path .. " " .. table.concat(paths, " ")
  local success, _ = pcall(run_command, cmd)
  if not success then
    error("ImageOptim optimisation failed or ImageOptim not found")
  end
end

-- Get B2 authorisation token
local function get_b2_auth()
  local auth_cmd = string.format(
    "curl -s -u %s:%s https://api.backblazeb2.com/b2api/v2/b2_authorize_account",
    M.config.b2_key_id,
    M.config.b2_key
  )
  local auth_response = run_command(auth_cmd)
  return vim.fn.json_decode(auth_response)
end

-- Upload file to B2
local function upload_to_b2(auth_data, file_path, file_name)
  local upload_url_cmd = string.format(
    "curl -s -H 'Authorization: %s' %s/b2api/v2/b2_get_upload_url --data '{\"bucketId\":\"%s\"}'",
    auth_data.authorizationToken,
    auth_data.apiUrl,
    auth_data.allowed.bucketId
  )

  local upload_url_response = vim.fn.json_decode(run_command(upload_url_cmd))

  local upload_cmd = string.format(
    "curl -s -H 'Authorization: %s' -H 'X-Bz-File-Name: %s' -H 'Content-Type: image/jpeg' -T %s %s",
    upload_url_response.authorizationToken,
    file_name,
    file_path,
    upload_url_response.uploadUrl
  )

  return vim.fn.json_decode(run_command(upload_cmd))
end

--- @param path string
--- @param alt_text string
--- @return string
function M.process_file(path, alt_text)
  if not vim.fn.filereadable(path) then
    error("File not found: " .. path)
  end

  local filename = vim.fn.fnamemodify(path, ":t")
  local name = vim.fn.fnamemodify(filename, ":r")
  local ext = vim.fn.fnamemodify(filename, ":e")

  -- Create temporary files
  local full_tmp = vim.fn.tempname() .. "." .. ext
  local thumb_tmp = vim.fn.tempname() .. "." .. ext

  -- Copy original file to temp files
  vim.fn.system(string.format("cp '%s' '%s'", path, full_tmp))
  vim.fn.system(string.format("cp '%s' '%s'", path, thumb_tmp))

  -- Process images
  scale_image(thumb_tmp)
  optimise_images({ full_tmp, thumb_tmp })

  -- Upload to B2
  local auth_data = get_b2_auth()
  local full_name = string.format("images/%s_full.%s", name, ext)
  local thumb_name = string.format("images/%s_thumb.%s", name, ext)

  local full_upload = upload_to_b2(auth_data, full_tmp, full_name)
  local thumb_upload = upload_to_b2(auth_data, thumb_tmp, thumb_name)

  -- Generate HTML
  local html = string.format(
    '<a href="%s%s"><img src="%s%s" alt="%s"></a>',
    M.config.bucket_prefix,
    full_upload.fileName,
    M.config.bucket_prefix,
    thumb_upload.fileName,
    alt_text
  )

  -- -- Copy to clipboard
  -- vim.fn.system("pbcopy", html)

  -- Clean up temp files
  os.remove(full_tmp)
  os.remove(thumb_tmp)

  return html
end

-- Setup function for the plugin
function M.setup(opts)
  M.config = vim.tbl_deep_extend("force", M.config, opts or {})
end

vim.api.nvim_create_user_command('UploadImage', function(opts)
  local path = opts.args
  local alt_text = vim.fn.input('Alt text: ')
  local html = M.process_file(path, alt_text)
  vim.api.nvim_put({html}, 'c', true, true)
  print("Image uploaded and inserted!")
end, {nargs = 1})

return M
