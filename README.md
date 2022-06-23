# RegexPerfTest
A small and simple perf test in python for comparing the performance of good and bad regexes. (rewrite in python)

## Install Dependencies

Install the python dependencies.

```sh
pip3 install re datetime json
```

## Edit regex_dico.json

Structure :
> Note: You can add / remove `regex and input` entries
```json
{
"regex" : {
"REGEX1" : ".*",
"REGEX2" : "[a-z]*"
},
"input" : {
"INPUT1" : "hello world"
},

"nb_runs" : 10000,
"file_log" : "/var/log/calc_regex.log"
}
```

# Run

Run the main script.

```sh
python3 regex_calculator.py
```

# Read output

Read the log file.
> Note: The path can be change in `json config file`
```sh
cat /var/log/calc_regex.log
```

Inspired (java) : https://github.com/zzbennett/RegexPerfTest
