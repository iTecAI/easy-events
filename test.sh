python3 -m uvicorn test.test-api.server:app --reload &
cd test/test-ui
yarn start | cat