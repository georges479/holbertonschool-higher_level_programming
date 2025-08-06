#!/usr/bin/node

const args = process.argv.slice(2).map(arg => parseInt(arg, 10));

if (args.length < 2) {
  console.log(0);
} else {
  const uniqueArgs = [...new Set(args)];
  uniqueArgs.sort((a, b) => b - a);
  console.log(uniqueArgs[1] || 0);
}
