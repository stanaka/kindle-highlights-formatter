1. Parse CLI arguments as options using argparse.
  a. details of options are written in Options section.
2. Parse My Clippings.txt
  a. The format of My Clippings.txt is shown below.
  b. Check when was the latest highlight for each book.
3. Extract contents to markdown format.
  a. Output contents to STDOUT.
  b. the format example should look like 'Output Markdown for the above example' section.
  c. Sort by the last highlight time. Output the latest one at first.
  d. No need to ignore ' <You have reached the clipping limit for this item>'
  e. If a highlight is empty or includes only spaces, then ignore the highlight.
4. Extract titles of books when 'titles' option is specified.
  a. Output titles of books to STDOUT.
  b. Output format example should look like "Output Markdown for the above example when 'titles' option is enabled.".
  c. Output only titles with the last highlighted time. Each line should start with the ordered number.
  d. Sorted by the last highlight time. Output the latest one at first.

## Options
- -h --help: display how to use the command
- -i --input FILE: use FILE as the input file. Default is "My Clippings.txt".
- -t --titles: display only titles of books
- -b --book NUMBER: only display contents for book NUMBER (where NUMBER corresponds to a value from the '--titles' option).

## Format of My Clippings.txt
```
私たちはなぜ税金を納めるのか―租税の経済思想史―（新潮選書） (諸富 徹)
- Your Highlight on Location 67-70 | Added on Wednesday, July 12, 2023 12:02:51 AM

1つめの引用
==========
私たちはなぜ税金を納めるのか―租税の経済思想史―（新潮選書） (諸富 徹)
- Your Highlight on Location 224-224 | Added on Friday, July 14, 2023 12:00:09 AM

2つめの引用
==========
日清・日露戦争をどう見るか　近代日本と朝鮮半島・中国 (ＮＨＫ出版新書) (原 朗)
- Your Highlight on page 80 | Location 1165-1177 | Added on Sunday, August 6, 2023 11:23:02 PM

3つめの引用 <You have reached the clipping limit for this item>
==========
日清・日露戦争をどう見るか　近代日本と朝鮮半島・中国 (ＮＨＫ出版新書) (原 朗)
- Your Highlight on page 89 | Location 1338-1352 | Added on Sunday, August 6, 2023 11:31:12 PM

 <You have reached the clipping limit for this item>
==========
日清・日露戦争をどう見るか　近代日本と朝鮮半島・中国 (ＮＨＫ出版新書) (原 朗)
- Your Highlight on page 94 | Location 1407-1413 | Added on Sunday, August 6, 2023 11:34:32 PM

 <You have reached the clipping limit for this item>
```

## Output Markdown for the above example when 'titles' option is enabled.
```
1. 私たちはなぜ税金を納めるのか―租税の経済思想史―（新潮選書） (諸富 徹) (Last highlighted: Friday, July 14, 2023 12:00:09 AM)
2. 日清・日露戦争をどう見るか　近代日本と朝鮮半島・中国 (ＮＨＫ出版新書) (原 朗) (Last highlighted: Sunday, August 6, 2023 11:31:12 PM)
```


## Output Markdown for the above example.
```
# 私たちはなぜ税金を納めるのか―租税の経済思想史―（新潮選書） (諸富 徹) (Last highlighted: Friday, July 14, 2023 12:00:09 AM)
- Location 67-70
> 1つめの引用
- Location 224-224
> 2つめの引用

# 日清・日露戦争をどう見るか　近代日本と朝鮮半島・中国 (ＮＨＫ出版新書) (原 朗) (Last highlighted: Sunday, August 6, 2023 11:31:12 PM)
- Page 80 | Location 1165-1177
> 3つめの引用 <You have reached the clipping limit for this item>
- Page 89 | Location 1338-1352
> <You have reached the clipping limit for this item>
- Page 94 | Location 1407-1413
> <You have reached the clipping limit for this item>
```
