cmake_minimum_required(VERSION 3.14)
project(ecef_to_geodetic LANGUAGES CXX)

find_package(pybind11 REQUIRED)

add_library(ecef_to_geodetic MODULE ecef_to_geodetic.cpp)

set_target_properties(ecef_to_geodetic PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED YES
    PREFIX ""
)

target_link_libraries(ecef_to_geodetic PRIVATE pybind11::module)
