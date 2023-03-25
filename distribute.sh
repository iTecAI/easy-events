python3 -m pip install build twine
cd python/easyevents

python3 -m build
python3 -m twine upload -r testpypi dist/*

cd ../../react/easy-events
yarn publish