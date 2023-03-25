"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Arc(google.protobuf.message.Message):
    """稿件基本信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AID_FIELD_NUMBER: builtins.int
    VIDEOS_FIELD_NUMBER: builtins.int
    TYPE_ID_FIELD_NUMBER: builtins.int
    TYPE_NAME_FIELD_NUMBER: builtins.int
    COPYRIGHT_FIELD_NUMBER: builtins.int
    PIC_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    PUBDATE_FIELD_NUMBER: builtins.int
    CTIME_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    STATE_FIELD_NUMBER: builtins.int
    ACCESS_FIELD_NUMBER: builtins.int
    ATTRIBUTE_FIELD_NUMBER: builtins.int
    TAG_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    MISSION_ID_FIELD_NUMBER: builtins.int
    ORDER_ID_FIELD_NUMBER: builtins.int
    REDIRECT_URL_FIELD_NUMBER: builtins.int
    FORWARD_FIELD_NUMBER: builtins.int
    RIGHTS_FIELD_NUMBER: builtins.int
    AUTHOR_FIELD_NUMBER: builtins.int
    STAT_FIELD_NUMBER: builtins.int
    REPORT_RESULT_FIELD_NUMBER: builtins.int
    DYNAMIC_FIELD_NUMBER: builtins.int
    FIRST_CID_FIELD_NUMBER: builtins.int
    DIMENSION_FIELD_NUMBER: builtins.int
    STAFF_INFO_FIELD_NUMBER: builtins.int
    SEASON_ID_FIELD_NUMBER: builtins.int
    ATTRIBUTE_V2_FIELD_NUMBER: builtins.int
    SEASON_THEME_FIELD_NUMBER: builtins.int
    SHORT_LINK_V2_FIELD_NUMBER: builtins.int
    UP_FROM_V2_FIELD_NUMBER: builtins.int
    FIRST_FRAME_FIELD_NUMBER: builtins.int
    aid: builtins.int
    """稿件avid"""
    videos: builtins.int
    """稿件分P数"""
    type_id: builtins.int
    """分区id"""
    type_name: builtins.str
    """二级分区名"""
    copyright: builtins.int
    """稿件类型
    1:原创 2:转载
    """
    pic: builtins.str
    """稿件封面url"""
    title: builtins.str
    """稿件标题"""
    pubdate: builtins.int
    """稿件发布时间"""
    ctime: builtins.int
    """用户投稿时间"""
    desc: builtins.str
    """稿件简介"""
    state: builtins.int
    """稿件状态"""
    access: builtins.int
    """访问属性
    0:全部可见 10000:登录可见
    """
    attribute: builtins.int
    """属性位配置(现在无了)"""
    tag: builtins.str
    """空"""
    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """空"""
    duration: builtins.int
    """稿件总时长(单位为秒)"""
    mission_id: builtins.int
    """参与的活动id"""
    order_id: builtins.int
    """绑定的商单id"""
    redirect_url: builtins.str
    """PGC稿件强制重定向url(如番剧、影视)"""
    forward: builtins.int
    """空"""
    @property
    def rights(self) -> global___Rights:
        """控制标志"""
    @property
    def author(self) -> global___Author:
        """UP主信息"""
    @property
    def stat(self) -> global___Stat:
        """状态数"""
    report_result: builtins.str
    """空"""
    dynamic: builtins.str
    """投稿时发送的动态内容"""
    first_cid: builtins.int
    """稿件1P cid"""
    @property
    def dimension(self) -> global___Dimension:
        """稿件1P 分辨率"""
    @property
    def staff_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StaffInfo]:
        """合作组成员列表"""
    season_id: builtins.int
    """UGC合集id"""
    attribute_v2: builtins.int
    """新版属性位配置(也没用)"""
    @property
    def season_theme(self) -> global___SeasonTheme:
        """"""
    short_link_v2: builtins.str
    """"""
    up_from_v2: builtins.int
    """"""
    first_frame: builtins.str
    """"""
    def __init__(
        self,
        *,
        aid: builtins.int = ...,
        videos: builtins.int = ...,
        type_id: builtins.int = ...,
        type_name: builtins.str = ...,
        copyright: builtins.int = ...,
        pic: builtins.str = ...,
        title: builtins.str = ...,
        pubdate: builtins.int = ...,
        ctime: builtins.int = ...,
        desc: builtins.str = ...,
        state: builtins.int = ...,
        access: builtins.int = ...,
        attribute: builtins.int = ...,
        tag: builtins.str = ...,
        tags: collections.abc.Iterable[builtins.str] | None = ...,
        duration: builtins.int = ...,
        mission_id: builtins.int = ...,
        order_id: builtins.int = ...,
        redirect_url: builtins.str = ...,
        forward: builtins.int = ...,
        rights: global___Rights | None = ...,
        author: global___Author | None = ...,
        stat: global___Stat | None = ...,
        report_result: builtins.str = ...,
        dynamic: builtins.str = ...,
        first_cid: builtins.int = ...,
        dimension: global___Dimension | None = ...,
        staff_info: collections.abc.Iterable[global___StaffInfo] | None = ...,
        season_id: builtins.int = ...,
        attribute_v2: builtins.int = ...,
        season_theme: global___SeasonTheme | None = ...,
        short_link_v2: builtins.str = ...,
        up_from_v2: builtins.int = ...,
        first_frame: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["author", b"author", "dimension", b"dimension", "rights", b"rights", "season_theme", b"season_theme", "stat", b"stat"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["access", b"access", "aid", b"aid", "attribute", b"attribute", "attribute_v2", b"attribute_v2", "author", b"author", "copyright", b"copyright", "ctime", b"ctime", "desc", b"desc", "dimension", b"dimension", "duration", b"duration", "dynamic", b"dynamic", "first_cid", b"first_cid", "first_frame", b"first_frame", "forward", b"forward", "mission_id", b"mission_id", "order_id", b"order_id", "pic", b"pic", "pubdate", b"pubdate", "redirect_url", b"redirect_url", "report_result", b"report_result", "rights", b"rights", "season_id", b"season_id", "season_theme", b"season_theme", "short_link_v2", b"short_link_v2", "staff_info", b"staff_info", "stat", b"stat", "state", b"state", "tag", b"tag", "tags", b"tags", "title", b"title", "type_id", b"type_id", "type_name", b"type_name", "up_from_v2", b"up_from_v2", "videos", b"videos"]) -> None: ...

global___Arc = Arc

@typing_extensions.final
class Author(google.protobuf.message.Message):
    """UP主信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    FACE_FIELD_NUMBER: builtins.int
    mid: builtins.int
    """UP主mid"""
    name: builtins.str
    """UP主昵称"""
    face: builtins.str
    """UP主头像url"""
    def __init__(
        self,
        *,
        mid: builtins.int = ...,
        name: builtins.str = ...,
        face: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["face", b"face", "mid", b"mid", "name", b"name"]) -> None: ...

global___Author = Author

@typing_extensions.final
class Dimension(google.protobuf.message.Message):
    """分辨率"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WIDTH_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    ROTATE_FIELD_NUMBER: builtins.int
    width: builtins.int
    """宽度"""
    height: builtins.int
    """高度"""
    rotate: builtins.int
    """方向
    0:横屏 1:竖屏
    """
    def __init__(
        self,
        *,
        width: builtins.int = ...,
        height: builtins.int = ...,
        rotate: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height", "rotate", b"rotate", "width", b"width"]) -> None: ...

global___Dimension = Dimension

@typing_extensions.final
class Page(google.protobuf.message.Message):
    """分P信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CID_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    FROM_FIELD_NUMBER: builtins.int
    PART_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    VID_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    WEBLINK_FIELD_NUMBER: builtins.int
    DIMENSION_FIELD_NUMBER: builtins.int
    FIRST_FRAME_FIELD_NUMBER: builtins.int
    cid: builtins.int
    """视频cid"""
    page: builtins.int
    """分P序号"""
    part: builtins.str
    """分P标题"""
    duration: builtins.int
    """分P时长(单位为秒)"""
    vid: builtins.str
    """外链vid"""
    desc: builtins.str
    """分P简介"""
    webLink: builtins.str
    """外链url"""
    @property
    def dimension(self) -> global___Dimension:
        """分P分辨率"""
    first_frame: builtins.str
    """"""
    def __init__(
        self,
        *,
        cid: builtins.int = ...,
        page: builtins.int = ...,
        part: builtins.str = ...,
        duration: builtins.int = ...,
        vid: builtins.str = ...,
        desc: builtins.str = ...,
        webLink: builtins.str = ...,
        dimension: global___Dimension | None = ...,
        first_frame: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["dimension", b"dimension"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["cid", b"cid", "desc", b"desc", "dimension", b"dimension", "duration", b"duration", "first_frame", b"first_frame", "from", b"from", "page", b"page", "part", b"part", "vid", b"vid", "webLink", b"webLink"]) -> None: ...

global___Page = Page

@typing_extensions.final
class Rights(google.protobuf.message.Message):
    """稿件控制标志"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BP_FIELD_NUMBER: builtins.int
    ELEC_FIELD_NUMBER: builtins.int
    DOWNLOAD_FIELD_NUMBER: builtins.int
    MOVIE_FIELD_NUMBER: builtins.int
    PAY_FIELD_NUMBER: builtins.int
    HD5_FIELD_NUMBER: builtins.int
    NO_REPRINT_FIELD_NUMBER: builtins.int
    AUTOPLAY_FIELD_NUMBER: builtins.int
    UGC_PAY_FIELD_NUMBER: builtins.int
    IS_COOPERATION_FIELD_NUMBER: builtins.int
    UGC_PAY_PREVIEW_FIELD_NUMBER: builtins.int
    NO_BACKGROUND_FIELD_NUMBER: builtins.int
    ARC_PAY_FIELD_NUMBER: builtins.int
    PAY_FREE_WATCH_FIELD_NUMBER: builtins.int
    bp: builtins.int
    """老版是否付费"""
    elec: builtins.int
    """允许充电"""
    download: builtins.int
    """允许下载"""
    movie: builtins.int
    """是否电影"""
    pay: builtins.int
    """PGC稿件需要付费"""
    hd5: builtins.int
    """是否高码率"""
    no_reprint: builtins.int
    """是否显示“禁止转载”标志"""
    autoplay: builtins.int
    """是否允许自动播放"""
    ugc_pay: builtins.int
    """UGC稿件需要付费(旧版)"""
    is_cooperation: builtins.int
    """是否联合投稿"""
    ugc_pay_preview: builtins.int
    """是否UGC付费预览"""
    no_background: builtins.int
    """是否禁止后台播放"""
    arc_pay: builtins.int
    """UGC稿件需要付费"""
    pay_free_watch: builtins.int
    """是否已付费可自由观看"""
    def __init__(
        self,
        *,
        bp: builtins.int = ...,
        elec: builtins.int = ...,
        download: builtins.int = ...,
        movie: builtins.int = ...,
        pay: builtins.int = ...,
        hd5: builtins.int = ...,
        no_reprint: builtins.int = ...,
        autoplay: builtins.int = ...,
        ugc_pay: builtins.int = ...,
        is_cooperation: builtins.int = ...,
        ugc_pay_preview: builtins.int = ...,
        no_background: builtins.int = ...,
        arc_pay: builtins.int = ...,
        pay_free_watch: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arc_pay", b"arc_pay", "autoplay", b"autoplay", "bp", b"bp", "download", b"download", "elec", b"elec", "hd5", b"hd5", "is_cooperation", b"is_cooperation", "movie", b"movie", "no_background", b"no_background", "no_reprint", b"no_reprint", "pay", b"pay", "pay_free_watch", b"pay_free_watch", "ugc_pay", b"ugc_pay", "ugc_pay_preview", b"ugc_pay_preview"]) -> None: ...

global___Rights = Rights

@typing_extensions.final
class SeasonTheme(google.protobuf.message.Message):
    """"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BG_COLOR_FIELD_NUMBER: builtins.int
    SELECTED_BG_COLOR_FIELD_NUMBER: builtins.int
    TEXT_COLOR_FIELD_NUMBER: builtins.int
    bg_color: builtins.str
    """"""
    selected_bg_color: builtins.str
    """"""
    text_color: builtins.str
    """"""
    def __init__(
        self,
        *,
        bg_color: builtins.str = ...,
        selected_bg_color: builtins.str = ...,
        text_color: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["bg_color", b"bg_color", "selected_bg_color", b"selected_bg_color", "text_color", b"text_color"]) -> None: ...

global___SeasonTheme = SeasonTheme

@typing_extensions.final
class StaffInfo(google.protobuf.message.Message):
    """合作成员信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MID_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    ATTRIBUTE_FIELD_NUMBER: builtins.int
    mid: builtins.int
    """成员mid"""
    title: builtins.str
    """成员角色"""
    attribute: builtins.int
    """属性位
    0:普通 1:赞助商金色标志
    """
    def __init__(
        self,
        *,
        mid: builtins.int = ...,
        title: builtins.str = ...,
        attribute: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["attribute", b"attribute", "mid", b"mid", "title", b"title"]) -> None: ...

global___StaffInfo = StaffInfo

@typing_extensions.final
class Stat(google.protobuf.message.Message):
    """状态数"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AID_FIELD_NUMBER: builtins.int
    VIEW_FIELD_NUMBER: builtins.int
    DANMAKU_FIELD_NUMBER: builtins.int
    REPLY_FIELD_NUMBER: builtins.int
    FAV_FIELD_NUMBER: builtins.int
    COIN_FIELD_NUMBER: builtins.int
    SHARE_FIELD_NUMBER: builtins.int
    NOW_RANK_FIELD_NUMBER: builtins.int
    HIS_RANK_FIELD_NUMBER: builtins.int
    LIKE_FIELD_NUMBER: builtins.int
    DISLIKE_FIELD_NUMBER: builtins.int
    aid: builtins.int
    """稿件avid"""
    view: builtins.int
    """播放数(当屏蔽时为-1)"""
    danmaku: builtins.int
    """弹幕数"""
    reply: builtins.int
    """评论数"""
    fav: builtins.int
    """收藏数"""
    coin: builtins.int
    """投币数"""
    share: builtins.int
    """分享数"""
    now_rank: builtins.int
    """当前排名"""
    his_rank: builtins.int
    """历史最高排名"""
    like: builtins.int
    """点赞数"""
    dislike: builtins.int
    """点踩数(前端不可见故恒为0)"""
    def __init__(
        self,
        *,
        aid: builtins.int = ...,
        view: builtins.int = ...,
        danmaku: builtins.int = ...,
        reply: builtins.int = ...,
        fav: builtins.int = ...,
        coin: builtins.int = ...,
        share: builtins.int = ...,
        now_rank: builtins.int = ...,
        his_rank: builtins.int = ...,
        like: builtins.int = ...,
        dislike: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aid", b"aid", "coin", b"coin", "danmaku", b"danmaku", "dislike", b"dislike", "fav", b"fav", "his_rank", b"his_rank", "like", b"like", "now_rank", b"now_rank", "reply", b"reply", "share", b"share", "view", b"view"]) -> None: ...

global___Stat = Stat
