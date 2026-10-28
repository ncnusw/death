"""Story script, quizzes, pauses and passwords for 書庫裡的光 Light in the Stacks. build_data.py imports this file.
Change the passwords and the discussion question here, then run build_data.py.
(The opening password is in ../index.html, look for GATE_PASSWORD.)
Content follows the Week 8 lecture, Grief Counseling & Prolonged Grief (08_week8.qmd), and its sources:
DSM-5-TR (APA, 2022); Prigerson et al. (2021, 2022); Bonanno & Malgaroli (2020); Schut & Stroebe (2005);
Johannsen et al. (2019); Larson & Hoyt (2007); Lundorff et al. (2017); Djelantik et al. (2020); Tsai et al. (2016);
Szuhany et al. (2021); Shear et al. (2005, 2014, 2016); Simon & Shear (2024); Eisma (2023).
The campus, 阿哲, 許老師 and everyone else are fictional."""

# Password that continues the story after the mid-game discussion (also a jump code on the title screen).
DISCUSS_PASSWORD = 'YEARNING'

DISCUSS_QUESTION = '''<p><b>阿哲符合 PGD 的哪幾項標準？哪些還需要專業人員確認？身為朋友（或社工），你可以做什麼？不應該做什麼？</b></p>
<p class="en">Which PGD criteria does Zhe seem to meet? Which still need a professional to check? As a friend (or a social worker), what can you do, and what should you not do?</p>'''

PAUSES = {
    'discuss1': {
        'head': '⏸ 討論時間 Discussion',
        'code': DISCUSS_PASSWORD,
        'html': DISCUSS_QUESTION + '''<p class="small">請放下手機，和旁邊的同學討論。老師公布密碼後，輸入密碼繼續。<br>
Put your phone down and discuss with your classmates. Enter the password from your teacher to continue.</p>'''},
}

JUMPS = {DISCUSS_PASSWORD: 'back_lib'}

# B3 time limit (the phone battery). The shortest route from the stairs to Zhe takes `steps` moves of 0.14 s.
# The dark, the dead ends and the shadows (which send you back to the stairs) all cost time, so most players
# should need one or two tries. Raise B3_SLACK to make it easier.
B3_SLACK = 3.0
def b3_seconds(steps, extra=1.0):
    return int(round((steps * 0.14 * B3_SLACK + 15) * extra))

# The eight Criterion C symptoms, as the shadows in the basement (DSM-5-TR wording, short form)
SHADOWS = {
    'b1': [('D:121', '逃避 Avoiding reminders'), ('D:108', '情緒麻木 Emotional numbness')],
    'b2': [('D:120', '強烈孤單 Intense loneliness'), ('D:121', '難以相信 Disbelief'), ('D:108', '人生沒有意義 Life feels meaningless')],
    'b3': [('D:121', '認同混亂 Identity disruption'), ('D:120', '強烈情緒痛苦 Intense emotional pain'), ('D:108', '難以重新投入 Trouble re-engaging')],
}
SHADOW_MS = {'b1': 430, 'b2': 380, 'b3': 330}

QUIZZES = {
    'q1': {'tag': '許老師的小考 1/11 · Part 1', 'q': '「很痛，但生活還能繼續。」大約 71% 喪偶者走的這條悲傷軌跡，英文叫什麼？',
           'options': ['prolonged grief', 'resilience', 'depression', 'avoidance'], 'answer': 1,
           'hint': '中文是「復原力」。', 'ok': '答對了！大部分人的悲傷雖然痛，卻是正常的。'},
    'q2': {'tag': '許老師的小考 2/11 · Part 1', 'q': '三層喪親照顧裡，只給「悲傷已經卡住」的人的專業治療，是哪一層？',
           'options': ['universal', 'selective', 'palliative', 'indicated'], 'answer': 3,
           'hint': '第三層：有「指標」顯示需要，才提供。'},
    'q3': {'tag': '許老師的小考 3/11 · Part 2', 'q': '「延續性哀傷障礙症」的英文是什麼？',
           'options': ['Persistent Complex Bereavement Disorder', 'Post-Traumatic Stress Disorder', 'Prolonged Grief Disorder', 'Major Depressive Disorder'], 'answer': 2,
           'hint': '是 2022 年 DSM-5-TR 的正式名稱。很像的那一個，是 2013 年附錄裡的舊名稱。'},
    'q4': {'tag': '許老師的小考 4/11 · Criterion A', 'q': '成人要在死亡之後至少多久，才可能診斷 PGD？',
           'options': ['2 weeks', '6 months', '12 months', '24 months'], 'answer': 2,
           'hint': '6 個月是兒童和青少年的標準。'},
    'q5': {'tag': '許老師的小考 5/11 · Criterion B', 'q': 'PGD 的核心症狀（強烈思念逝者，和／或一直想著逝者），英文是什麼？',
           'options': ['yearning and/or preoccupation', 'fear and hypervigilance', 'low mood and loss of interest', 'guilt and anger'], 'answer': 0,
           'hint': '「思念」是 yearning。'},
    'q6': {'tag': '許老師的小考 6/11 · Criterion C', 'q': '一個人說：「我的一部分，好像也跟著她死了。」這是 Criterion C 的哪一項？',
           'options': ['disbelief', 'identity disruption', 'emotional numbness', 'intense loneliness'], 'answer': 1,
           'hint': '他對「我是誰」的感覺，被打亂了。'},
    'q7': {'tag': '許老師的小考 7/11 · Criterion C', 'q': '一個人寒假不敢回家，因為看到逝者的房間會受不了。這是哪一項？',
           'options': ['life feels meaningless', 'emotional numbness', 'avoiding reminders', 'trouble re-engaging'], 'answer': 2,
           'hint': '他在躲開會「想起」逝者的東西。'},
    'q8': {'tag': '許老師的小考 8/11 · PGD、憂鬱、PTSD', 'q': 'PGD、憂鬱症、PTSD 常常一起出現。PTSD 的核心感受是什麼？',
           'options': ['fear', 'yearning', 'low mood', 'loneliness'], 'answer': 0,
           'hint': 'PTSD 的心思在「危險或事件」上。'},
    'q9': {'tag': '許老師的小考 9/11 · Part 3', 'q': '篩檢 PGD 的量表（10 題症狀，總分 30 分以上可能是 PGD）叫什麼？',
           'options': ['PHQ-9', 'DSM-5-TR', 'PGDT', 'PG-13-R'], 'answer': 3,
           'hint': '名字裡有 PG（Prolonged Grief）和 13。'},
    'q10': {'tag': '許老師的小考 10/11 · 社工的角色', 'q': '社工遇到可能有 PGD 的人，該做什麼？',
            'options': ['diagnose and prescribe', 'screen and refer', 'wait a few more years', 'tell them to move on'], 'answer': 1,
            'hint': '社工篩檢，不下診斷；診斷交給精神科醫師或心理師。'},
    'q11': {'tag': '許老師的小考 11/11 · 治療', 'q': '實證最多、大約 16 次、在「面對失落」和「重建生活」之間來回擺盪的治療，叫什麼？',
            'options': ['citalopram', 'psychological debriefing', 'PGDT (Prolonged Grief Disorder Therapy)', 'a support group'], 'answer': 2,
            'hint': '以前叫 CGT（complicated grief treatment）。', 'ok': '答對了！藥物幫助的是憂鬱，不是悲傷。'},
}

SCRIPT = r'''
// ======================= OPENING: WEEK 8 LECTURE =======================
:: intro
@save
@clear
@tint none
@music quiet
@player me
@title 死亡、悲傷與喪親照顧 · 第八週|Death, Grief, and Bereavement Care · Week 8
{{CLASSROOM}}
@put teacher D:88 classroom 10 2 cls_teacher
@map classroom 16 18 up
Teacher: Good morning, everyone. Last week, we learned to walk alongside the mourner.
Teacher: This week: how to notice when grief gets stuck, and what helps.
> 投影片上寫著：Grief Counseling & Prolonged Grief。
@goal 和旁邊的同學說說話（頭上有 ! 的同學）。

:: cls_teacher
Teacher: Most bereaved people are resilient. Grief is painful, but grief is not a disorder.
> 你在筆記本上寫下：resilient。

:: cls_a
@label s{{A}} cls_done
Classmate: 「Prolonged grief disorder」……悲傷也可以是一種「疾病」嗎？
Classmate: 我阿嬤過世的時候，我爸難過了好久好久。那樣算嗎？
@goto cls_count

:: cls_b
@label s{{B}} cls_done
Classmate: 我昨天打工到半夜一點……老師的英文聽起來好像催眠曲。
> 他說完，就趴在桌上睡著了。
@goto cls_count

:: cls_c
@label s{{C}} cls_done
Classmate: 欸，你還記得大一的阿哲嗎？常常一個人坐在圖書館角落的那個。
Classmate: 他後來好像就很少來上課了……
> 你愣了一下。你當然記得。
@goto cls_count

:: cls_done
> Zzz……

:: cls_count
@inc talked
@if talked>=3 cls_drift

:: cls_drift
Teacher: Criterion B is the core: yearning for the person who died, or preoccupation with them...
> 「yearning」……你看著窗外的圖書館。
> 三年前的那個下午，你也曾經從阿哲身邊走過，什麼也沒說。
> 你的眼皮越來越重……
@tint sepia
> 老師的聲音越來越遠。冷氣的聲音，慢慢變成了翻書的聲音……
@goto lib1

// ======================= THE LIBRARY, THREE YEARS AGO =======================
:: lib1
@save
@clear
@tint sepia
@music quiet
@player me
@title 三年前 · 圖書館|Three years ago · The library
@put librarian lin library 6 12 lib_librarian0
@put s1 v7 library 11 4 lib_student
@put s2 v2 library 13 10 lib_student2
@put zhe hao library 21 13 lib_zhe !
@put poster X:12 library 10 15 lib_poster0
@zone cin counsel 0 0 13 9 c_enter
@door library/basement lock 樓梯口的牌子寫著：「地下書庫 B1–B3」。大一的你，從來沒有下去過。
@door library/out lock 等一下……那天下午，阿哲就坐在角落。先去看看他。
@map library 12 14 up
> 你睜開眼睛。這裡不是教室，是學校的圖書館。
> 陽光從窗戶斜斜地照進來。一切都和三年前一模一樣。
@goal 去找坐在角落的阿哲（右下角）。

:: lib_student
Classmate: （小聲）噓……期中考快到了。

:: lib_student2
> 這位同學戴著耳機，正在趕報告。

:: lib_librarian0
Librarian: 同學，要借書嗎？

:: lib_poster0
> 公告欄上貼著好幾張海報：社團招生、講座、二手書市集……

:: lib_zhe
@label zhe lib_zhe2
> 阿哲坐在角落的位子。桌上攤著一本書，可是他一頁也沒有翻。
> 他一直盯著手機上的一張照片。
Me: 阿哲？好久不見。你最近都沒來上課……
Zhe: ……喔，是你。
Zhe: 我沒事啦。只是這裡比較安靜。
@choice
? 「好，那我不吵你了。」 -> lib_zhe_leave
? 「你看起來很累。最近還好嗎？」 -> lib_zhe_ask

:: lib_zhe_leave
> 三年前的你，就是這樣說的。然後你轉身走開了。
> 可是這一次，你停下腳步，又回頭看了他一眼。
@goto lib_zhe_after

:: lib_zhe_ask
Zhe: 真的沒事。……你去忙你的吧。
> 他把手機螢幕蓋了起來，轉頭看向窗外。
@goto lib_zhe_after

:: lib_zhe_after
Me (VO): 他不是「沒事」。可是……我不知道該怎麼辦。我又不是心理師。
@label librarian lib_librarian !
@goal 問問櫃台旁的館員阿姨。

:: lib_zhe2
> 阿哲還是盯著那張照片。

:: lib_librarian
@label librarian lib_librarian2
Librarian: 那個男生啊？這學期幾乎每天都來，從開館坐到閉館。
Librarian: 很少看到他借書，也很少看到他跟誰說話。
Librarian: 聽說他媽媽去年過世了……走得很突然。
Librarian: 你是他朋友吧？如果擔心他，可以去學生諮商中心問問老師。門口的公告欄有寫。
@label poster lib_poster !
@goal 看看門口的公告欄（大門左邊）。

:: lib_librarian2
Librarian: 學生諮商中心就在圖書館隔壁。

:: lib_poster
@label poster lib_poster2
> 公告欄上有一張淡藍色的海報：
> 「學生諮商中心｜心情卡卡的時候，歡迎來聊聊。擔心朋友嗎？也歡迎你來問：『我可以怎麼幫他？』」
Me (VO): 我可以先去問問，要怎麼幫阿哲。
@door library/out counsel 6 7
@goal 走出圖書館大門（下面），到隔壁的學生諮商中心。

:: lib_poster2
> 「擔心朋友嗎？也歡迎你來問：『我可以怎麼幫他？』」

// ======================= THE COUNSELING CENTER =======================
:: c_enter
@goto counsel_scene

:: counsel_scene
@save
@clear
@tint none
@music warm
@player me
@put hsu v3 counsel 4 3 hsu1 !
@door counsel/out lock 先和許老師聊聊。
@map counsel 6 7 up
> 你推開諮商中心的門。四周的顏色，好像慢慢亮了起來。
Me (VO): 這一次，我想做點不一樣的事。
@goal 和許老師說話（沙發旁邊）。

:: hsu1
@label hsu -
Hsu: 你好，我是許老師，這裡的諮商心理師。請坐。
Me: 老師……我不是自己要諮商。我是擔心一個朋友。
Hsu: 很好啊，很多同學都是這樣來的。說說看？
Me: 他叫阿哲。他媽媽去年突然過世，到現在大概一年兩個月了。
Me: 他每天坐在圖書館角落，不太上課，也不太跟人說話……他是不是生病了？他需要諮商嗎？
Hsu: 好問題。在回答之前，我先跟你說一件很重要的事。
@title 第一部分：誰需要悲傷輔導？|Part 1 · Who needs grief counseling?
Hsu: 有一個研究，追蹤了 282 位喪偶的人兩年多。你猜，大部分的人後來怎麼了？
@choice
? 大部分的人都需要接受治療。
? 大部分的人雖然很難過，但慢慢恢復了正常生活。
? 大部分的人一輩子都走不出來。
@if choice=2 hsu1_right
Hsu: 其實剛好相反。
@goto hsu1_b

:: hsu1_right
Hsu: 沒錯。
@goto hsu1_b

:: hsu1_b
Hsu: 大約 71% 的人很有**復原力（resilience）**：很痛，但生活還能繼續。大約 24% 的人一開始比較辛苦，後來慢慢改善。
Hsu: 只有大約 5% 的人，悲傷一直卡住，沒有好轉。
Hsu: 所以，**悲傷不是疾病**。大部分的悲傷，雖然痛，卻是正常的。
@quiz q1
Hsu: 我們的工作是：支持每一個人，同時**找出**那些卡住的人。
Hsu: 喪親照顧有三層。第一層是**普遍性（universal）**支持，給每一個喪親的人：陪伴、資訊。
Hsu: 第二層是**選擇性（selective）**支持，給風險比較高的人，例如支持團體。
Hsu: 第三層是**指標性（indicated）**介入，給悲傷已經卡住的人：專業的悲傷治療。
@quiz q2
Hsu: 研究也發現：越需要的人，治療越有幫助。針對悲傷障礙症狀的心理治療，效果最大；對一般的悲傷，效果就小很多。
Hsu: 你也許聽過「悲傷輔導會讓 38% 的人變得更糟」。那個數字來自一篇沒有發表的論文，沒有可靠的根據。
Me: 所以重點不是每個人都要諮商，而是找到卡住的人。
Hsu: 對。那阿哲，是不是卡住了？我們到白板那邊，看看診斷標準。
@move hsu 7 2
@label hsu hsu2 !
@goal 到白板前，和許老師說話。

:: hsu2
@label hsu -
@title 第二部分：延續性哀傷障礙症|Part 2 · Prolonged Grief Disorder (PGD)
Hsu: 2022 年，美國精神醫學會的 DSM-5-TR，正式加入了一個診斷：**延續性哀傷障礙症（Prolonged Grief Disorder, PGD）**。
Hsu: 2013 年的 DSM-5，只把它放在附錄，叫「持續性複雜喪慟障礙症」，意思是還需要更多研究。
@quiz q3
Hsu: 診斷標準有 A 到 F 六項。我們用阿哲來練習。不過要記得：我們是在學習，不是在幫朋友下診斷。
Hsu: **Criterion A**：死亡至少已經過了 12 個月。兒童和青少年是 6 個月。
Hsu: 阿哲的媽媽，過世多久了？
@choice
? 一年兩個月，超過 12 個月了。
? 八個月，還不到。
@if choice=2 hsu_a_wrong
Hsu: 對，A 符合。
@goto hsu_a_done

:: hsu_a_wrong
Hsu: 你剛剛說的是一年兩個月喔。那就超過 12 個月了，A 符合。
@goto hsu_a_done

:: hsu_a_done
Hsu: 如果只有八個月，就算他很難過，也不能診斷 PGD。我們會支持他，然後繼續關心。
@quiz q4
Hsu: **Criterion B** 是核心：強烈**思念（yearning）**逝者，和／或一直**想著（preoccupation）**逝者。
Hsu: 在兒童和青少年身上，也可能是一直想著，死亡是怎麼發生的。
Me: 阿哲一直盯著手機上的照片……館員阿姨說，他每天都坐在那裡。
@quiz q5
Hsu: **Criterion C**：下面八項中，至少要有三項。
Hsu: 一、**認同混亂（identity disruption）**：好像自己的一部分也死了。二、**難以相信（disbelief）**死亡真的發生了。
Hsu: 三、**逃避（avoiding reminders）**會想起逝者的事物。四、**強烈的情緒痛苦（intense emotional pain）**，例如憤怒、苦澀、哀傷。
Hsu: 五、**難以重新投入（trouble re-engaging）**人際關係和活動。六、**情緒麻木（emotional numbness）**。
Hsu: 七、覺得**人生沒有意義（life feels meaningless）**。八、**強烈的孤單（intense loneliness）**。
Hsu: B 和 C 的症狀，要在最近至少一個月裡，幾乎每天都出現。
Me: 阿哲符合幾項，我其實不知道……
Hsu: 那就問他，聽他自己怎麼說。先來練習看看。
@quiz q6
@quiz q7
Hsu: **Criterion D**：造成明顯的痛苦，或影響到生活功能，例如課業、工作、人際。
Hsu: **Criterion E**：明顯超出他所在的社會、文化或宗教，對哀悼的一般期待。
Hsu: **Criterion F**：不能用其他問題解釋得更好，例如憂鬱症或創傷後壓力症（PTSD）。
Me: 憂鬱症和 PGD，不是很像嗎？
Hsu: 常常一起出現，所以三種都要篩檢。可是核心不一樣：
Hsu: PGD 的核心是**思念**：心思在逝者身上，會逃避想起失落的事物。
Hsu: 憂鬱症是**心情低落、失去樂趣**：心思在自己和所有的事情上。PTSD 是**害怕**：心思在危險或事件上，會逃避想起危險的事物。
@quiz q8
Hsu: PGD 多常見？自然死亡之後，大約**十分之一**的喪親成人；自殺、他殺、意外、災難這些非自然的死亡之後，大約**二分之一**。
Hsu: 臺灣有一個研究，追蹤 493 位癌末病人的家屬：六個月時 7.7%，十三個月以後大約只剩 2%。大部分的家屬都恢復了。
Hsu: 哪些人風險比較高？失去孩子或伴侶；突然或暴力的死亡；沒有機會好好道別；死亡之前就有憂鬱或精神疾病；社會支持很少；對死亡沒有準備。
Me: 阿哲的媽媽是突然中風走的。館員阿姨說，他好像沒來得及見到最後一面。
Hsu: 那就有兩個風險因素：突然的死亡、沒有機會道別。
Hsu: 也有人擔心：把悲傷變成診斷，會不會把正常的難過當成病？會不會給人壓力，要人「趕快走出來」？會不會讓人想用藥物處理悲傷？
Hsu: 所以標準裡有保護措施：要等 12 個月、要超出文化的常模、要影響生活，也要和憂鬱症、PTSD 分開。
Hsu: 好，最後一部分。我們到桌子那邊。
@move hsu 10 3
@label hsu hsu3 !
@goal 到桌子旁，和許老師說話。

:: hsu3
@label hsu -
@title 第三部分：評估與介入|Part 3 · Assessment & treatment
Hsu: 篩檢可以用 **PG-13-R** 量表：10 題症狀，每題 1 到 5 分，總分 10 到 50。
Hsu: 總分 30 分以上，加上死亡已經超過 12 個月、生活功能受到影響，就是「可能是 PGD」，要轉介去做完整的評估。
@quiz q9
Hsu: 社工的角色有三件事：**篩檢（screen），不下診斷**；**轉介（refer）**給精神科醫師或心理師；還有，**問自殺**，因為 PGD 會提高自殺的風險。
Me: 問自殺……不會反而讓他想到嗎？
Hsu: 不會。直接、溫和地問，不會讓人更想自殺。不問，才可能錯過需要幫助的人。
@quiz q10
Hsu: 治療方面，實證最多的是 **PGDT（延續性哀傷障礙症治療）**，大約 16 次，以前叫 CGT。
Hsu: 它在「面對失落」和「重建生活」之間來回擺盪：說出死亡的故事、慢慢面對會想起逝者的事物、和回憶連結；也看見有希望的未來、重新建立關係。
Me: 這不就是我們學過的雙軌擺盪模式嗎？
Hsu: 沒錯。
Hsu: 那吃藥呢？一個 395 人的研究：悲傷治療加抗憂鬱劑，和悲傷治療加安慰劑，效果差不多（83.7% 和 82.5%）。
Hsu: 藥物幫助的是憂鬱，不是悲傷。到現在，還沒有任何藥物被核准用來治療 PGD。
Hsu: 其他有實證的方法還有：以悲傷為焦點的認知行為治療、從安寧療護就開始的家庭悲傷治療，以及給兒童和青少年的認知行為治療。
@quiz q11
Hsu: 好。回到阿哲。你不需要幫他診斷，也不需要當他的治療師。
Hsu: 他需要的是：有人注意到他、陪著他、聽他說，然後，陪他來這裡。
@pause discuss1
Hsu: 去吧。我在這裡等你們。
@goto back_lib

// ======================= BACK TO THE LIBRARY =======================
:: back_lib
@save
@clear
@tint none
@music quiet
@player me
@put librarian lin library 6 12 back_librarian !
@put s1 v7 library 11 4 lib_student
@put book X:14 library 21 13 back_seat
@put zhe hao b3 {{ZX}} {{ZY}} b3_zhe !
@set b1seen 0
@set b2seen 0
@set b3seen 0
@zone zb1 b1 0 0 99 99 b1_in
@zone zb2 b2 0 0 99 99 b2_in
@zone zb3 b3 0 0 99 99 b3_in
@door library/basement lock 先問問館員阿姨，阿哲去哪裡了。
@door library/out lock 阿哲還沒找到。
@map library 12 14 up
> 你帶著許老師教你的東西，回到圖書館。
> 角落的位子……空了。椅子旁邊只剩下他的背包。
@goal 問館員阿姨：阿哲去哪裡了？

:: back_seat
> 阿哲的背包。拉鍊沒拉上，裡面露出一張期中考的缺考單。

:: back_librarian
@label librarian back_librarian2
Librarian: 阿哲？他剛剛往地下書庫走了。
Librarian: 下面有三層，B1、B2、B3，都是舊書和舊期刊。平常幾乎沒有人下去。
Librarian: 地下室的燈這幾天壞了，還在等人來修。裡面黑漆漆的，書架又排得像迷宮一樣。
Me: 我去找他。
Librarian: 小心一點。用手機的手電筒吧。
@item 手機手電筒 Phone flashlight
@door library/basement b1 1 1
@goal 走下樓梯（右上角），到地下書庫找阿哲。

:: back_librarian2
Librarian: 樓梯在右上角。小心腳步。

// ======================= THE LOWER STACKS =======================
:: b1_in
@if b1seen=1 b1_lit
@set b1seen 1
@tint none
@music stop
@light 2.8
{{MOBS}}
@door b1/up lock 阿哲還在下面。
@door b2/up lock 阿哲還在更下面。
@door b3/up lock 阿哲就在這一層。
@set fails 0
> 手電筒只照得亮身邊一小圈。書架一排一排，把地下室排成了迷宮。
> 黑暗裡，有東西在動。
Me (VO): 那是……影子？
Me (VO): 許老師說，悲傷本身不是病，也不是敵人。大部分的人，悲傷再痛，也會慢慢走過來。
Me (VO): 可是這些影子不一樣。它們是讓悲傷「卡住」的東西，就像 Criterion C 的那八項。
Me (VO): 碰到它們，我就會被逼回樓梯口。要看準時機，避開它們。
@goal B1：避開影子，找到往 B2 的樓梯（右下角）。

:: b1_lit
@light 2.8

:: hit_b1
> 「{hit}」的影子把你團團圍住。好冷……
> 你退回樓梯口，深呼吸，再試一次。
@pos 1 1 down

:: b2_in
@if b2seen=1 b2_lit
@set b2seen 1
@light 2.7
@sound wow
> B2。空氣更冷了。
Me (VO): 孤單、不敢相信、覺得人生沒有意義……阿哲每天，都帶著這些影子過日子嗎？
@goal B2：避開影子，找到往 B3 的樓梯（左下角）。

:: b2_lit
@light 2.7

:: hit_b2
> 「{hit}」的影子擋住了你的路。你看不見前面了……
> 你退回樓梯口，再試一次。
@pos {{B2X}} 1 down

:: b3_in
@if b3seen=1 b3_go
@set b3seen 1
@music danger
@sound wow
> B3，最底層。這裡的書架又高又密。
> 你的手機跳出一個通知：
Phone: 【電量不足】剩下 10%。
Me (VO): 手電筒撐不了多久了。在手機沒電之前，一定要找到阿哲！
@goto b3_go

:: b3_go
@light 3.0
@goal B3：在手機沒電之前，找到阿哲！
@if fails>=2 b3_go_long
@timer {{B3_SECONDS}} b3_fail fade

:: b3_go_long
@timer {{B3_SECONDS_LONG}} b3_fail fade

:: hit_b3
> 「{hit}」的影子撲了過來！你退回樓梯口。
> 手機的電量，還在一點一點往下掉……
@pos 1 1 down

:: b3_fail
@inc fails
> 手機螢幕一黑。四周什麼都看不見了。
> 你摸著書架，慢慢走回樓梯口。還好，口袋裡有行動電源……充一點電，再試一次。
@put zhe hao b3 {{ZX}} {{ZY}} b3_zhe !
@map b3 1 1 down
@if fails>=2 b3_hint

:: b3_hint
Me (VO): 冷靜。路是固定的，每走一次，我就更熟悉這裡。
Me (VO): 阿哲一直想躲開所有人……他應該在最深、最裡面的角落。

:: b3_zhe
@timer off
@music quiet
@unmob all
@sound wow
@label zhe -
> 阿哲坐在最裡面的角落，背靠著書架。手機螢幕上，是他媽媽的照片。
Zhe: ……你怎麼會在這裡？
@goto z_open

:: z_open
Me (VO): 要怎麼開口？
@choice
? 「都一年多了，你也該走出來了吧。」 -> z_bad1
? 「我有點擔心你。我可以坐在你旁邊嗎？」 -> z_good1

:: z_bad1
Zhe: ……連你也這樣說。我爸也這樣說。
> 阿哲把頭轉開，不說話了。
Me (VO): 不對。「趕快走出來」只會給他壓力。這也正是大家擔心把悲傷當成疾病的原因之一。
Me (VO): 每個人悲傷的路不一樣長。重來一次。
@goto z_open

:: z_good1
Zhe: ……嗯。
> 你在他旁邊坐下。過了很久，他才開口。
Zhe: 去年這個時候，我媽突然中風。我在學校接到電話，趕回去的時候，已經來不及了。
Zhe: 我連再見都沒有說。
Zhe: 我每天都好想她。睡前一直看她傳給我的訊息，一遍又一遍。
Zhe: 我不敢回家，寒假也沒有回去。看到她的房間，我會受不了。
Zhe: 有時候覺得，我的一部分好像也跟著她走了。上課、系隊……好像都沒有意義了。
Me (VO): 思念，一直想著她：這是 B。認同混亂、逃避、覺得沒有意義、難以重新投入、孤單：C 已經超過三項了。
Me (VO): 已經超過 12 個月，也影響到課業：A 和 D。
Me (VO): 可是我不是醫師，也不是心理師。我能做的是……
@choice
? 「你可能是 PGD，延續性哀傷障礙症。」 -> z_bad2
? 「謝謝你告訴我。聽起來，這一年你一個人扛了好多。」 -> z_good2

:: z_bad2
Me (VO): 等一下。我不能幫他下診斷。診斷是精神科醫師或心理師的工作。
Me (VO): 現在，他需要的是有人聽他說。
@goto z_good2

:: z_good2
Me: 謝謝你告訴我。聽起來，這一年你一個人扛了好多。
Zhe: ……嗯。
Me (VO): 許老師說，還有一件事一定要問。PGD 會提高自殺的風險。
@choice
? 不要問，怕問了反而讓他想到。 -> z_bad3
? 直接、溫和地問他。 -> z_good3

:: z_bad3
Me (VO): 不對。直接、溫和地問，不會讓人更想自殺。不問，才可能錯過。
@goto z_good3

:: z_good3
Me: 阿哲，我想問你一件事，你可以照實說。你有沒有想過，要結束自己的生命？
Zhe: ……沒有。我沒有想要死。
Zhe: 我只是覺得好累。什麼都提不起勁。
Me: 謝謝你願意跟我說實話。如果哪一天，你有了這種念頭，一定要馬上告訴我，或告訴諮商中心的老師，好嗎？
Zhe: ……好。
Me: 學校的學生諮商中心有心理師，可以陪你聊聊媽媽，也可以一起想想接下來怎麼走。
Me: 不用錢，談的內容也會保密。
Zhe: 去諮商……是不是代表我有病？
@choice
? 「對，你需要治療，越快越好。」 -> z_bad4
? 「不是。悲傷不是病。只是你一個人卡在這裡太久了。」 -> z_good4

:: z_bad4
Me (VO): 這樣說，好像在幫他貼標籤。換個說法。
@goto z_good4

:: z_good4
Me: 不是。悲傷不是病。你這麼想你媽媽，是因為你愛她。
Me: 只是你一個人在這裡，卡了太久。有人陪著，會比較好走。
Me: 我陪你一起去，好嗎？那邊的許老師人很好。
Zhe: ……你會陪我去？
Me: 嗯。我們一起上去。
> 阿哲把手機收進口袋，慢慢站了起來。
@title 你們一起，一層一層走上樓梯|Together, you climb back up, one floor at a time
@goto ending

// ======================= ENDING =======================
:: ending
@save ending
@clear
@tint dusk
@music warm
@player me
@put librarian lin library 6 12 end_librarian
@put zhe hao library 22 3 -
@put hsu v3 counsel 6 3 end_hsu !
@door library/basement lock 不用再下去了。
@door library/out counsel 6 7
@door counsel/out lock 先陪阿哲找許老師。
@map library 21 2 down
@follow zhe
> 回到一樓，窗外的天已經黑了。
@goal 陪阿哲走到學生諮商中心（圖書館大門出去），找許老師。

:: end_librarian
Librarian: 找到了啊……太好了。

:: end_hsu
@label hsu -
@follow off
Hsu: 你是阿哲吧？我是許老師。謝謝你願意來。
Hsu: （轉頭對你）也謝謝你陪他來。
Hsu: 阿哲，我們先到裡面坐一下，聊聊你和媽媽的事。等一下，我也會請你填一份簡短的問卷。
Hsu: 如果需要，我們也會一起找適合你的協助。你不用一個人想辦法。
Zhe: ……好。
Zhe: （轉頭對你）謝謝你下來找我。
@move hsu 9 3
@move zhe 8 3
@del zhe
@del hsu
> 諮商室的門輕輕關上了。接下來的談話，是屬於阿哲的。
Me (VO): 我不能替他走完這段路。但至少，他不再是一個人了。
@sound win
@title 叮咚——|Ding-dong—
@goto wake

:: wake
@clear
@tint none
@music quiet
{{CLASSROOM_PLAIN}}
@put teacher D:88 classroom 10 2 -
@map classroom 16 18 up
> 你猛然醒來。投影片已經換到最後一頁。
Teacher: Key takeaways. One: most grief is normal. Don't treat everyone.
Teacher: Two: PGD means at least twelve months, plus yearning, plus at least three of eight symptoms, plus impairment.
Teacher: Three: screen, ask about suicide, and refer.
Teacher: Four: grief-focused therapy works. Pills don't treat grief.
> 你拿出手機，找到那個很久沒有聯絡的名字。
> 你打了一行字：「阿哲，好久不見。最近好嗎？」
@end
'''
