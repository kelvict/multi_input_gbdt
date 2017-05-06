cmake_minimum_required(VERSION 3.5)
project(kaggle_2014_criteo)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    solvers/gbdt/src/common.cpp
    solvers/gbdt/src/common.h
    solvers/gbdt/src/gbdt.cpp
    solvers/gbdt/src/gbdt.h
    solvers/gbdt/src/timer.cpp
    solvers/gbdt/src/timer.h
    solvers/gbdt/src/train.cpp
    solvers/libffm-1.13/ffm-predict.cpp
    solvers/libffm-1.13/ffm-train.cpp
    solvers/libffm-1.13/ffm.cpp
    solvers/libffm-1.13/ffm.h)

add_executable(kaggle_2014_criteo ${SOURCE_FILES})