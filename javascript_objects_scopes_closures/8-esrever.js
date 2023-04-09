#!/usr/bin/node
'use strict';


/**
 * esrever
 * @param {array} list - List of elements
 * @exemple esrever([1, 2, 3]) => [3, 2, 1]
 */
exports.esrever = list => {
    let new_list = [];

    for ( let i = list.length - 1; i >= 0; i--)
    {

        const element = list[i];
        new_list.push(element)

    }

    return new_list
}
