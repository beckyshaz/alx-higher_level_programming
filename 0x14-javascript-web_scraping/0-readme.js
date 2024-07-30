#!/usr/bin/node
// Reading a file using fs module
const filepath = process.argv[2];
const fs = require('fs');
fs.readFile(filepath, { encoding: 'utf-8' }, function (err, data) {
  if (err) {
    return console.error('Error', err);
  }
  console.log(data);
});
