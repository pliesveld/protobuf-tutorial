#!/bin/bash

rm -rf myproto/ build/ dist/
mkdir myproto
find protobuf/ -name '*.proto' -exec protoc --python_out=myproto/ -Iprotobuf {} \;
touch myproto/__init__.py
