#!/usr/bin/node
'use strict';


/**
 * converter
 * @param {number} base - New base number
 * @exemple converter(2)
 */
exports.converter = base => {
    
    return number => {

        return parseInt(number, base);

    }

}
