// @ts-check
import { exec } from "child_process";
import { promisify } from "util";

const execAsync = promisify(exec);

/**
 * Gets a list of all commits in the current git repository
 * @returns {Promise<Array<{ date: Date, hash: string }>>} Array of commit information
 */
export async function getCommits() {
  const { stdout } = await execAsync('git log --pretty=format:"%H %aI"');
  return stdout
    .trim()
    .split("\n")
    .map((line) => {
      const [hash, date] = line.split(" ");
      return {
        hash,
        date: new Date(date),
      };
    });
}
