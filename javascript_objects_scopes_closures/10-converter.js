#!/usr/bin/node
'use strict';


/**
 * converter
 * @param {number} base - New base number
 * @exemple converter(2)
 */
exports.converter = base => {
    
    const convert_base = number => {

        return parseInt(number, base);

    }
    
    return convert_base;

}
