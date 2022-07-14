// To answer the question "How does the `resolve` function of a promise affect
// control flow, and what happens if you resolve multiple times?"
// Next: What happens if you resolve and reject, in either order?

const main = async () => {
  const result = await new Promise(resolve => {
    for (let i = 0; i < 5; i++) {
      console.log(`Resolving ${i}`);
      resolve(i)
    }
    console.log("Resolved 5 times");
  })

  console.log(`Outside the promise, the result is ${result}`);
}

main().then(process.exit)
