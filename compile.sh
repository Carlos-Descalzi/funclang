#!/bin/bash

java -jar antlr4.jar FuncLang.g4 -o funclang -visitor  -Dlanguage=Python3
