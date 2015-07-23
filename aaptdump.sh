#!/bin/bash

./aapt d badging $* | egrep "package:|application-label:|application:"
