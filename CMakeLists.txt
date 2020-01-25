cmake_minimum_required(VERSION 3.2)

add_executable(ip_filter src/ip_filter.cpp)

set_target_properties(ip_filter PROPERTIES
    CXX_STANDARD 14
    CXX_STANDARD_REQUIRED ON
)
