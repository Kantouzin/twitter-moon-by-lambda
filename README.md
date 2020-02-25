# Twitter Moon by Lambda

Understand the moon phase!

🌑 🌒 🌛 🌓 🌔 🌕 🌖 🌗 🌜 🌘 🌑

## Description

This project is for AWS Lambda.

Add the day's phase of the moon to your Twitter profile location.


## Requirement

- [rackerlabs/lambda-uploader](https://github.com/rackerlabs/lambda-uploader)
  - [requirements.txt](requirements.txt)
  - `lambda.json`
- [HDE/python-lambda-local](https://github.com/HDE/python-lambda-local)
  - [lambda-local/test.sh](lambda-local/test.sh)
  - [lambda-local/event.json](lambda-local/event.json)
  - `lambda-local/config.json`

This project is missing `lambda.json` and `lambda-local/config.json` (because include access key).
You need to add AWS Lambda settings and environment variables (Twitter `CONSUMER_KEY`, etc.).

## License

[MIT license](LICENSE)
