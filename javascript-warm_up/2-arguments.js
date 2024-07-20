#!/usr/bin/node
const { argv } = require('process');

if (argv === 0) {
    console.log('No argument');
    }
    else if (argv[0]) {
        console.log('Argument found');
    }
    else {
        console.log('Arguments found');
    }
