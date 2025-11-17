# Steps

1. Install chrome

```sh
npx @puppeteer/browsers install chrome@142.0.7444.162
```

2. Get chrome path to update the executable_path

```sh
npx @puppeteer/browsers list
```

3. Start the server

```sh
 python3 -m http.server 8000
```

4. Run the automation

```sh
 uv run test_upload_resume.py --resume resume.pdf
```
