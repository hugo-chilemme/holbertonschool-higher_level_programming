#!/usr/bin/node
'use strict';

/**
 * esrever
 * @param {array} list - List of elements
 * @exemple esrever([1, 2, 3]) => [3, 2, 1]
 */
exports.esrever = list => {
  const newList = [];

  for (let i = list.length - 1; i >= 0; i--) {
    const element = list[i];
    newList.push(element);
  }

  return newList;
};
