set -eux

PROJECT=$1
PKG_NAME=$2

USER=mikealexeevotus
REPONAME=otus-cpp
BINTRAY_URL=https://api.bintray.com/content
PUBLISH_ARGS='deb_distribution=trusty;deb_component=main;deb_architecture=amd64;publish=1'

version="0.0.${TRAVIS_BUILD_NUMBER}"
deb_file=${PKG_NAME}-${version}-Linux.deb

curl -T "${deb_file}" \
    -u "${USER}:${BINTRAY_API_KEY}" \
    "${BINTRAY_URL}/{$USER}/${REPONAME}/${PROJECT}/${TRAVIS_BUILD_NUMBER}/${deb_file};${PUBLISH_ARGS}"
