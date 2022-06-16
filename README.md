# Twitter Moon by Lambda

<div align="center">
  Understand the moon phase!

  🌑 🌒 🌛 🌓 🌔 🌕 🌖 🌗 🌜 🌘 🌑
</div>

## Description

This project is for AWS Lambda.

Add the day's phase of the moon to your Twitter profile location.

## Requirement

- [Serverless Framework](https://www.serverless.com/)

This project is missing `serverless.yml` (because include access key).
You need to add environment variables (Twitter `CONSUMER_KEY`, etc.).

## Run

```bash
sls invoke --function function --log
```

## Deploy

```bash
sls deploy
```

## License

[MIT license](LICENSE)
