alias="docker-compose run --rm dev bash"

setup() {
    echo "Set up $1"
    mkdir "$1"
    touch "$1/sample.py"
    touch "$1/$1.md"
}