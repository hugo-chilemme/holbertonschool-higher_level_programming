#!/usr/bin/node
'use strict';


/**
 * nbOccurences
 * @param {array} list - List of elements
 * @param {char} searchElement = Element to search
 * @exemple nbOccurences([1, 2, 3], 3)
 */
exports.nbOccurences = (list, searchElement) => {
    let occurrences = 0;

    for ( const element of list )
    {

        if ( element === searchElement )
        {

            occurrences += 1;

        }

    }

    return occurrences
}
