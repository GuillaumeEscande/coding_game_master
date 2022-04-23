#!/bin/bash

usage(){
    echo "merger.sh [-l <lib project name>]* [-o <file folder path>] <src project name>"
}

OUTPUT="target"
LIBS=()


while getopts ":o:l:h" option; do
    case "${option}" in
        h)
            usage
            exit 1
            ;;
        o)
            OUTPUT="${OPTARG}"
            ;;
        l)
            LIBS+=("${OPTARG}")
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

SRC="$@"

echo "OUTPUT=${OUTPUT}"
echo "SRC=${SRC}"
echo "LIBS=${LIBS[@]}"

mkdir -p ${OUTPUT}

OUTPUT_SRC="${OUTPUT}/main.py"

echo "#### AUTOMATICALY - GENERATED  ####" > "${OUTPUT_SRC}"

for LIB in ${LIBS[@]}
do
    for file in $(ls ./libs/$LIB/src/*.py)
    do
        cat $file >> "${OUTPUT_SRC}"
        echo "" >> "${OUTPUT_SRC}"
    done
done


for file in $(ls ./game/${SRC}/src/*.py)
do
    cat $file >> "${OUTPUT_SRC}"
    echo "" >> "${OUTPUT_SRC}"
done


for LIB in ${LIBS[@]}
do
    sed -i "s|^from $LIB.*||g" "${OUTPUT_SRC}"
done


for file in $(ls ./game/${SRC}/src/*.py)
do
    filename=$(basename -- "$file")
    filename="${filename%.*}"
    sed -i "s|^from $filename.*||g" "${OUTPUT_SRC}"
done

set -x

# Remove comments
perl -i -0pe 's|#.*||g' "${OUTPUT_SRC}"

# Remove empty lines
perl -i -0pe 's|^\s*\n||gms' "${OUTPUT_SRC}"

# Remove indexation
perl -i -0pe 's|    | |g' "${OUTPUT_SRC}"
