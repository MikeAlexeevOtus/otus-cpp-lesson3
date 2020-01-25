cmake_minimum_required(VERSION 3.2)

set(TRAVIS_BUILD_NUMBER $ENV{TRAVIS_BUILD_NUMBER})
if(NOT TRAVIS_BUILD_NUMBER)
    set(TRAVIS_BUILD_NUMBER 1)
endif()

project(ip_filter VERSION 0.0.${TRAVIS_BUILD_NUMBER})

add_executable(ip_filter src/ip_filter.cpp)

add_executable(timus_1000 timus/1000.cpp)
add_executable(timus_1001 timus/1001.cpp)

set_target_properties(ip_filter timus_1001 PROPERTIES
    CXX_STANDARD 14
    CXX_STANDARD_REQUIRED ON
)

if (MSVC)
    set(COMPILE_OPTS /W4)
else ()
    set(COMPILE_OPTS -Wall -Wextra -pedantic -Werror)
endif()

target_compile_options(ip_filter PRIVATE ${COMPILE_OPTS})
target_compile_options(timus_1001 PRIVATE ${COMPILE_OPTS})

install(TARGETS ip_filter RUNTIME DESTINATION bin)

set(CPACK_GENERATOR DEB)

set(CPACK_PACKAGE_VERSION_MAJOR "${PROJECT_VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${PROJECT_VERSION_MINOR}")
set(CPACK_PACKAGE_VERSION_PATCH "${PROJECT_VERSION_PATCH}")

set(CPACK_PACKAGE_CONTACT mike.42.alexeev@yandex.ru)

include(CPack)
