// Ref: https://developer.mozilla.org/en-US/docs/Web/API/FileReader#Properties
const FILE_READER_DONE_STATE = 2;

/**
 * Generate a data URL for a given file. I've tested this in a browser;
 * might also work in node/deno/etc.
 *
 * @param {File} file
 * @return {Promise<string>}
 */
export default async function generateDataUrl(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    // This handler is untested because I'm not sure how one could even get
    // an error here. However, according to
    // https://developer.mozilla.org/en-US/docs/Web/API/FileReader,
    // `FileReader` does call the `onerror` handler and has an `error`
    // property of type `DOMError`.
    reader.onerror = () => reject(reader.error);

    reader.onload = () => {
      if (reader.readyState === FILE_READER_DONE_STATE) {
        resolve(reader.result);
      } else {
        reject("Unexpected error reading file");
      }
    };
    reader.readAsDataURL(file);
  });
}
