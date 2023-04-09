#!/usr/bin/node
'use strict';


/**
 * class Rectangle
 */
class Rectangle {

    /**
     * constructor
     * @param {number} w - Width
     * @param {number} h - Height
     * new Rectangle(2, 3);
     */
    constructor(w, h) {

        
        // When rectangle values are valid
        if ( w > 0 && h > 0 )
        {

            this.width = w;
            this.height = h;
            
        }


    }


}

module.exports = Rectangle
