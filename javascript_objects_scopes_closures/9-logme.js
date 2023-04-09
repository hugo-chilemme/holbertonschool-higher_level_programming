#!/usr/bin/node
'use strict';


/**
 * esrever
 * @param {string} item - Message
 * @exemple esrever([1, 2, 3]) => [3, 2, 1]
 */
let logMeList = [];
exports.logMe = item => {
    
    console.log(`${logMeList.length}: ${item}`);
    logMeList.push(item);

}
