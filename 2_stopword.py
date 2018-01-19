#!/usr/bin/env python
# -*- coding: utf-8  -*-
#去除停用词
import codecs,sys

def stopWord(sourceFile,targetFile,stopkey):
    sourcef = codecs.open(sourceFile, 'r')
    targetf = codecs.open(targetFile, 'w')
    print('open source file: '+ sourceFile)
    print('open target file: '+ targetFile)
    lineNum = 1
    line = sourcef.readline()
    while line:
        print('---processing ',lineNum,' article---')
        sentence = delstopword(line,stopkey)
        #print sentence
        targetf.writelines(sentence + '\n')       
        lineNum = lineNum + 1
        line = sourcef.readline()
    print('well done.')
    sourcef.close()
    targetf.close()
    

#删除停用词
def delstopword(line,stopkey):
    wordList = line.split(' ')          
    sentence = ''
    for word in wordList:
        word = word.strip()
        if word not in stopkey:
            if word != '\t':
                sentence += word + " "
    return sentence.strip()


if __name__ == '__main__':
    stopkey = [w.strip() for w in codecs.open('stopWord.txt', 'r').readlines()]
    
    sourceFile = 'positive_cut.txt'
    targetFile = 'positive_cut_stopword.txt'
    stopWord(sourceFile,targetFile,stopkey)

    sourceFile = 'negtive_cut.txt'
    targetFile = 'negtive_cut_stopword.txt'
    stopWord(sourceFile,targetFile,stopkey)