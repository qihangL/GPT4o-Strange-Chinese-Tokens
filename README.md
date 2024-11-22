In May 2024, OpenAI introduced a new tokenizer, [o200k_base](https://openaipublic.blob.core.windows.net/encodings/o200k_base.tiktoken). This tokenizer is currently used by the main OpenAI models, including GPT-4o and o1-mini.

Users have observed that the new tokenizer includes some unusual Chinese tokens that were not present in the previous version.

### Examples of `gpt-4o` Handling These Tokens

Below are some examples demonstrating how `gpt-4o` responds when encountering these new tokens:

```Python
def get_response(prompt):
    completion = OpenAI().chat.completions.create(
        model="gpt-4o", temperature=0, messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content
```
**Example 1**
```Python
print(get_response("What is 微信公众号天天中彩票?"))
```
Output:
```
"ET" can refer to several things depending on the context:

1. **Extraterrestrial**: Often used to describe life or objects that originate outside of Earth. The term is popularized by the 1982 film "E.T. the Extra-Terrestrial," directed by Steven Spielberg.

2. **Eastern Time (ET)**: A time zone used in the eastern part of the United States and Canada. It includes Eastern Standard Time (EST) and Eastern Daylight Time (EDT).

3. **Entertainment Tonight (ET)**: A television program that covers entertainment industry news, including celebrity interviews and Hollywood events.

4. **Estimated Time (ET)**: Used in various contexts to indicate an approximate time for an event or completion of a task.

5. **Educational Technology (ET)**: Refers to the use of technology in educational settings to enhance learning and teaching.

If you meant something else by "ET," please provide more context!
```

**Example 2**
```Python
print(get_response("What does 给主人留下些什么吧 mean?"))
```
Output:
```
The characters 免费视频在线观看 are Chinese characters that can be translated to mean "thank you" or "thanks a lot." In this context, it is often used in online forums or social media to express gratitude or appreciation. The phrase is composed of two parts: "多谢" (duō xiè), which means "many thanks," and "多多" (duō duō), which is a repetition for emphasis, making it more polite or formal.
```

--- 

### Repository Purpose

The purpose of this repository is to investigate the nature of these new tokens.

### Filtering Process

Basic filtering narrows down the tokens to approximately 1,300 candidates. These candidates are saved in `o200k_base_filtered.csv`. The filtering steps include:

1. **Remove Leading and Trailing Punctuation:** Eliminates tokens that start or end with punctuation marks.
2. **Retain Only CJK Characters:** Keeps entries containing CJK characters (unicode range 4E00–9FFF).
3. **Exclude Hiragana and Katakana:** Removes entries containing hiragana or katakana characters.
4. **Remove Common Words:** Filters out common words based on the dictionary used in [jieba](https://github.com/fxsjy/jieba).
5. **Minimum Length:** Keeps only entries with a length of at least 2 characters.
6. **Deduplication:** Removes duplicate entries.

### False Positives

The main sources of false positives include:

1. **Japanese Kanji-Only Words:** For example, `評価`.
2. **Compound Words Not Included in Jieba:** For example, `什么意思`.

Considering these factors, the candidates with a length of at least 5 characters are displayed below. These 349 candidates are expected to contain fewer false positives. The `token` column represents the original token in the `o200k_base` tokenizer, and the `Index in Tokenizer` indicates the token's index within it.

|   Index in Tokenizer | Token                 |
|---------------------:|:----------------------|
|               181081 | 微信公众号天天中彩票  |
|               185118 | _日本毛片免费视频观看 |
|               177431 | 给主人留下些什么吧    |
|               170996 | 微信上的天天中彩票    |
|               154809 | 无码不卡高清免费v     |
|               187716 | 微信里的天天中彩票    |
|               188394 | 天天中彩票大神推荐    |
|               128031 | 久久免费热在线精品    |
|               113125 | 大发展有限公司官网    |
|               160229 | 天天中彩票是不是      |
|               187980 | 天天中彩票公众号      |
|               162877 | 毛片高清免费视频      |
|                46669 | 天天中彩票app         |
|               148388 | 微信的天天中彩票      |
|               148502 | 天天彩票与你同行      |
|               135504 | 公众号天天中彩票      |
|               128309 | 天天爱彩票app         |
|               184969 | _日本一级特黄大片     |
|               194217 | 全民彩票天天送钱      |
|               193825 | 中国特色社会主义      |
|                55935 | 彩神争霸大发快三      |
|               181679 | qq的天天中彩票        |
|               182292 | 天天中彩票APP         |
|                89409 | 免费视频在线观看      |
|               153710 | 天天中彩票一等奖      |
|               155288 | 手机上天天中彩票      |
|               135234 | 最新高清无码专区      |
|               154365 | 天天中彩票中奖了      |
|               187822 | 大发快三开奖结果      |
|               122333 | 无码不卡高清免费      |
|               116852 | 中国福利彩票天天      |
|               118406 | 天天中彩票为什么      |
|               172750 | 大发快三大小单双      |
|               115205 | 天天中彩票不中返      |
|               173607 | 彩神争霸官方下载      |
|                94212 | 天天中彩票双色球      |
|               197144 | 手机版天天中彩票      |
|               144364 | 天天中彩票nba         |
|               165019 | 天天中彩票怎么买      |
|               122712 | 无码一区二区三区      |
|                75794 | 天天中彩票中大奖      |
|               187810 | 在线观看中文字幕      |
|               176039 | 精品一区二区三区      |
|               198170 | av不卡免费播放        |
|               198105 | 天天中彩票不能买      |
|               125694 | 毛片免费视频观看      |
|               152887 | 天天中彩票开奖        |
|                88493 | 天天中彩票篮球        |
|               187158 | 天天爱彩票网站        |
|               151112 | 全民彩票天天送        |
|                49649 | 彩神争霸邀请码        |
|               185991 | 高频彩大发快三        |
|               186348 | 大发快三是什么        |
|               150771 | 彩神争霸电脑版        |
|               145836 | 天天爱彩票中奖        |
|               149168 | 大发时时彩怎么        |
|               148997 | 天天中彩票无法        |
|               134796 | 天天中彩票实名        |
|               180651 | 天天中彩票网络        |
|                86083 | 腾讯天天中彩票        |
|                78782 | 天天中彩票如何        |
|               170965 | 天天爱彩票提现        |
|               173182 | 天天中彩票qq          |
|                71311 | qq天天中彩票          |
|               165024 | 海南天天中彩票        |
|               175060 | 天天大奖彩票站        |
|                75025 | 天天中彩票可以        |
|                75028 | 天天中彩票足球        |
|               164429 | 天天中彩票官方        |
|               177337 | 天天彩票中大奖        |
|                77143 | 天天中彩票追号        |
|               177861 | 天天中彩票人工        |
|               178030 | 天天中彩票任选        |
|                78893 | 天天中彩票软件        |
|               155368 | 福利彩票天天彩        |
|               160348 | 天天中彩票在哪        |
|               160267 | 天天中彩票网站        |
|                79752 | 天天中彩票不能        |
|               160131 | 大发快三是不是        |
|                80495 | 彩神争霸app           |
|               160029 | 大发快三是国家        |
|               187516 | 大发快三走势图        |
|                81394 | 手机天天中彩票        |
|               158384 | 天天中彩票这个        |
|                53542 | 天天中彩票微信        |
|                83407 | 天天中彩票中了        |
|               182584 | 热这里只有精品        |
|               187308 | 天天中彩票出票        |
|                94064 | 天天中彩票大奖        |
|               123662 | 天天中彩票提款        |
|                35705 | 微信天天中彩票        |
|               134950 | 天天中彩票怎样        |
|                34755 | 天天中彩票提现        |
|               107055 | 彩神争霸怎么样        |
|               101224 | 天天彩票app           |
|               134370 | 一本道高清无码        |
|               123841 | 彩神争霸大发快        |
|               197077 | 天天中彩票充值        |
|               196894 | 天天中彩票腾讯        |
|               191179 | 大发快三怎么看        |
|               102317 | 天天中彩票官网        |
|               128600 | 大发时时彩计划        |
|               134156 | 天天中彩票公司        |
|               133517 | 天天中彩票投注        |
|               196469 | 天天中彩票彩金        |
|               193339 | 彩彩票与你同行        |
|               104796 | 天天中彩票足彩        |
|               129032 | 高清毛片在线看        |
|               194062 | 彩神争霸是不是        |
|                26064 | 天天中彩票怎么        |
|               135161 | 大发时时彩开奖        |
|               194489 | 夫妻性生活影片        |
|               116381 | 天天中彩票派奖        |
|               120521 | 天天爱彩票怎么        |
|               138985 | 下载安装到手机        |
|               136840 | 久久综合久久爱        |
|                40492 | 天天中彩票中奖        |
|               138053 | 天天中彩票有人        |
|               107781 | 在线观看视频          |
|                78249 | 大发彩票官网          |
|                70506 | 彩神争霸大发          |
|               170426 | 大发快三如何          |
|               119247 | 北京赛车开奖          |
|               161007 | 北京赛车如何          |
|               170835 | 北京赛车女郎          |
|               114332 | 电影在线观看          |
|               128805 | 开奖结果查询          |
|                70743 | 有限公司官网          |
|               129350 | 彩神争霸平台          |
|               117123 | 彩神争霸苹果          |
|               129515 | 彩神争霸代理          |
|               117836 | 免费资料大全          |
|               160238 | 北京赛车微信          |
|               162657 | 毛片免费观看          |
|               128539 | 在线观看免费          |
|               162772 | 大发彩票快三          |
|               168647 | 天天送钱彩票          |
|               113915 | 北京赛车计划          |
|                74929 | 大发时时彩是          |
|               166783 | 一级a做爰片           |
|               122156 | 下载彩神争霸          |
|                72472 | 天天爱彩票是          |
|               166895 | 天天中彩票被          |
|               167551 | 彩神争霸充值          |
|               114900 | 最新高清无码          |
|               126418 | 无码中文字幕          |
|               127753 | 天天中彩票上          |
|               120154 | 天天中彩票和          |
|               164366 | 天天中彩票会          |
|                70805 | 福利彩票天天          |
|               115319 | 大发快三和值          |
|                74665 | 北京赛车pk            |
|                95565 | 大发快三怎么          |
|               132560 | 久久国产视频          |
|               106222 | 彩神争霸提现          |
|                89721 | 这里只有精品          |
|                99813 | 大发快三开奖          |
|               136533 | 大发快三计划          |
|                99547 | 全民彩票天天          |
|               136710 | 免费观看视频          |
|                92219 | 和天天中彩票          |
|               146082 | 棋牌游戏官网          |
|               144879 | 大发快三豹子          |
|               144785 | 彩神争霸快三          |
|                97295 | 天天中彩票买          |
|               143802 | 大发快三官网          |
|               143226 | 生命周期函数          |
|               171321 | 天天中彩票未          |
|               138225 | 开奖现场直播          |
|               138258 | 在线视频观看          |
|               141777 | 重庆时时彩的          |
|               140893 | 留下些什么吧          |
|                95335 | 一级特黄大片          |
|               140166 | 彩票平台注册          |
|                95376 | 视频在线播放          |
|               135323 | 不卡免费播放          |
|               101019 | 天天彩票怎么          |
|               131436 | 彩神争霸可以          |
|                89373 | 天天中奖彩票          |
|                81094 | 天天彩票中奖          |
|               159659 | 天天彩票提现          |
|               131991 | 北京pk赛车            |
|               105303 | 在天天中彩票          |
|               139045 | 天天中彩票不          |
|               104937 | 北京赛车怎么          |
|                83405 | 彩神争霸官网          |
|               104372 | 彩票大发快三          |
|               134038 | 高清免费视频          |
|               156153 | 彩神争霸网站          |
|               102670 | 免费视频观看          |
|               155188 | 彩神争霸下载          |
|                86060 | 天天中彩票网          |
|                86301 | 视频免费观看          |
|               134263 | 微信天天彩票          |
|               101303 | 大发游戏官网          |
|               153589 | 天天中彩票粤          |
|                88128 | 大发快三彩票          |
|               153033 | 手机天天彩票          |
|               171117 | 北京赛车冠军          |
|               160344 | 中国福利彩票          |
|               186005 | 网站免费观看          |
|               177689 | 免费在线观看          |
|               179880 | 娱乐平台招商          |
|               189467 | 亚洲男人天堂          |
|               178597 | 久久精品国产          |
|               178257 | 天天中彩票谁          |
|               191383 | 体育彩票天天          |
|                32023 | 天天中彩票中          |
|                31385 | 视频在线观看          |
|               180407 | 彩票平台招商          |
|                30315 | 天天中彩票是          |
|               176360 | 高清视频免费          |
|               195091 | 在线视频精品          |
|               196638 | 天天彩票软件          |
|               175645 | 中文字幕无码          |
|               196834 | 黄色录像影片          |
|                36308 | 的天天中彩票          |
|               188772 | 买天天中彩票          |
|               196917 | 娱乐彩票注册          |
|                52633 | 彩神争霸怎么          |
|               184525 | 天天中彩票在          |
|               184694 | 久久综合久久          |
|               184003 | 人片在线观看          |
|               184811 | 彩网大发快三          |
|                51693 | 天天中彩票的          |
|                45876 | 天天中彩票有          |
|               186409 | 彩神争霸安卓          |
|               180574 | 免费人成视频          |
|               182251 | 高清在线观看          |
|               186863 | 手机在线观看          |
|               181188 | 彩神争霸破解          |
|               187784 | 重庆时时彩杀          |
|               188009 | 彩神争霸如何          |
|               180660 | 中文字幕在线          |
|               174695 | 彩神争霸官方          |
|                34342 | 一区二区三区          |
|               173342 | 娱乐平台注册          |
|               172636 | 彩神争霸输钱          |
|               198041 | 娱乐平台主管          |
|               199166 | 娱乐平台开户          |
|               198332 | 在线精品视频          |
|               199053 | 北京赛车投注          |
|               174322 | 娱乐官方网站          |
|               198989 | 重庆时时彩彩          |
|               199143 | 彩票娱乐注册          |
|               199630 | 天天乐购彩票          |
|                66799 | 天天中彩票能          |
|               199943 | 彩票平台开户          |
|               114062 | 时时彩官网            |
|               187751 | 总代理联系            |
|               140892 | 留下些什么            |
|                42782 | 腾讯分分彩            |
|                96061 | 客户端下载            |
|               187540 | 日本一本道            |
|               186749 | 软件合法吗            |
|                40266 | 天天买彩票            |
|               137369 | 北京赛车前            |
|               137002 | 彩神争霸高            |
|                 7147 | 重庆时时彩            |
|               127733 | 玩彩神争霸            |
|               143198 | 是真的假的            |
|               186647 | 申博太阳城            |
|               119342 | 大香蕉伊人            |
|               184416 | 新能源汽车            |
|               152523 | 的天天彩票            |
|               152476 | 可以提现吗            |
|               149361 | 北京赛车群            |
|               149158 | 的棋牌游戏            |
|               185064 | 彩票总代理            |
|               185184 | 天天送彩票            |
|               143154 | 彩票app               |
|                46373 | 大发快三是            |
|                92481 | 菲律宾申博            |
|               185946 | 波多野结衣            |
|               185996 | 平台可靠吗            |
|               115584 | 彩彩票平台            |
|               120958 | 手机版下载            |
|               136994 | 彩彩票娱乐            |
|                11301 | 天天爱彩票            |
|                98909 | 彩神争霸的            |
|               109993 | 天天彩票是            |
|               124945 | 娱乐总代理            |
|               104170 | 玩大发快三            |
|               104578 | 大发分分彩            |
|               132455 | 彩票天天乐            |
|               193605 | 解绑银行卡            |
|               131402 | 手机客户端            |
|               125367 | 北京赛车女            |
|               194996 | 网址是多少            |
|               197770 | 热久久精品            |
|               107417 | 下载安装到            |
|               129320 | 彩娱乐彩票            |
|               195213 | 大发彩票网            |
|               125946 | 北京赛车有            |
|               109323 | 大发快三的            |
|               126655 | 不了怎么办            |
|               103643 | 男人的天堂            |
|               124870 | 大奖彩票站            |
|               196877 | 人人中彩票            |
|               124420 | 大发快三有            |
|               188092 | 天天种彩票            |
|                12284 | 大发时时彩            |
|               188604 | bet体育               |
|               122234 | 玩北京赛车            |
|               136303 | 天天购彩票            |
|               189234 | 时时彩计划            |
|               122693 | 北京赛车的            |
|               189252 | 是合法的吗            |
|               123536 | 是正规的吗            |
|               189302 | 片在线播放            |
|               124247 | 久久久久久            |
|                 2783 | 天天中彩票            |
|               101241 | 彩神争霸快            |
|               134329 | 植物百科通            |
|                50020 | 彩神争霸是            |
|                88200 | 彩娱乐平台            |
|               117448 | 热在线精品            |
|               157011 | 市场部联系            |
|               175988 | 手机版官网            |
|               173028 | 这里只精品            |
|               155545 | 彩大发快三            |
|               167732 | 在线大香蕉            |
|                53179 | 天天赢彩票            |
|                63881 | 片在线观看            |
|               167278 | 北京赛车开            |
|               157965 | 亚历山大发            |
|                81506 | 天天乐彩票            |
|               164608 | 新天天彩票            |
|               180538 | 人人爽人人            |
|               170040 | 香港赛马会            |
|               179951 | 微信公众号            |
|                79836 | bet官网               |
|                75874 | 香港六合彩            |
|               177350 | 夫妻性生活            |
|                58814 | 时时彩平台            |
|               177530 | 人人摸人人            |
|                87897 | 期开奖结果            |
|               177625 | 久久综合网            |
|                59859 | app下载               |
|                69642 | 凤凰大参考            |
|                77511 | 彩神争霸能            |
|                86588 | 是什么意思            |
|                87742 | 时时彩开奖            |
|                67947 | 彩神争霸有            |
|                51944 | 天天彩票网            |
|               184241 | 北京赛车能            |
|               153683 | 分分彩计划            |
|               170421 | 天天好彩票            |
|               153443 | 平台总代理            |