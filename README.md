Test project
======================================

Set the following ENV variables:

- `TST_BASE_URL` (e.g. https://test.trunomi.com)
- `TST_DRIVER` (e.g. chrome)
- `TST_HTTP_TEST_URL` (e.g. http://www.trunomi.com)

Optional
To run tests against grid

- `TST_SELENIUM` (selenium grid url)  
To run tests in chrome headless mode
- `TST_HEADLESS` true

Solutions:

- Test plan draft refer to: test_plan document
- Http test /tests/test_http/test_1.py

    Test fail on puropose to ilustrate 
    independats run with parameters /tests/test_params.py

- UI test /tests/test_ui/test_ui_1.py
If test pass id written in new_dt_ids file

 