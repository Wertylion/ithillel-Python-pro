#!/bin/bash

echo "Скільки вам років?"
read age

if [ $age -ge 18 ]
then
    echo "Ви повнолітній"
else
    echo "Ви неповнолітній"
fi