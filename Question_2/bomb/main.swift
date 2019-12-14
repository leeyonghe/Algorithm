//
//  main.swift
//  bomb
//
//  Created by lee on 2019/12/15.
//  Copyright © 2019 lee. All rights reserved.
//

import Foundation

var linenum : Int = 0

var column : Int = 0

var row : Int = 0

var box = [[String]]()

while let readString = readLine() {
    
    if readString.isEmpty {
        break
    }
    
    if linenum == 0 {
        
        let array_type = readString.split(separator: " ")
        
        column = Int(array_type[0])!
        
        row = Int(array_type[1])!
        
    } else {
        
        let text = readString.trimmingCharacters(in: .whitespacesAndNewlines)
        var group = [String]()
        for t in text {
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>> \(String(t))")
            if String(t) == "*" {
                group.append(String(t))
            }else{
                group.append("0")
            }
        }
        box.append(group)
        
    }
    
    linenum += 1
    
}

print(">>>>>>>>>>>>>>>>>>>>>>>>>>> \(box)")

var result = [[String]](repeating: [String](repeating: "0", count: column), count: row)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>> \(result)")

for i in 0...row-1 {
    for j in 0...column-1 {
        if box[i][j] != "*" {
            let index : [[Int]] = [[i-1,j-1],[i,j-1],[i+1,j-1],[i-1,j],[i+1,j],[i-1,j+1],[i,j+1],[i+1,j+1]]
            var count = 0;
            for k in 0...7 {
                let x = index[k][0]
                let y = index[k][1]
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>> x = \(x)")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>> y = \(y)")
                if x >= 0 && y >= 0 && x < row && y < column && box[x][y] == "*" {
                    count += 1
                }
            }
            result[i][j] = String(count)
        }else{
            result[i][j] = "*"
        }
    }
}

print(">>>>>>>>>>>>>>>>>>>>>>>>>>> \(result)")
