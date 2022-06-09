"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AdInfo(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CREATIVE_ID_FIELD_NUMBER: builtins.int
    CREATIVE_TYPE_FIELD_NUMBER: builtins.int
    CARD_TYPE_FIELD_NUMBER: builtins.int
    CREATIVE_CONTENT_FIELD_NUMBER: builtins.int
    AD_CB_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    REQUEST_ID_FIELD_NUMBER: builtins.int
    IS_AD_FIELD_NUMBER: builtins.int
    CM_MARK_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    IS_AD_LOC_FIELD_NUMBER: builtins.int
    CARD_INDEX_FIELD_NUMBER: builtins.int
    CLIENT_IP_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    CREATIVE_STYLE_FIELD_NUMBER: builtins.int
    creative_id: builtins.int
    """"""

    creative_type: builtins.int
    """"""

    card_type: builtins.int
    """"""

    @property
    def creative_content(self) -> global___CreativeContent:
        """"""
        pass
    ad_cb: typing.Text
    """"""

    resource: builtins.int
    """"""

    source: builtins.int
    """"""

    request_id: typing.Text
    """"""

    is_ad: builtins.bool
    """"""

    cm_mark: builtins.int
    """"""

    index: builtins.int
    """"""

    is_ad_loc: builtins.bool
    """"""

    card_index: builtins.int
    """"""

    client_ip: typing.Text
    """"""

    extra: builtins.bytes
    """"""

    creative_style: builtins.int
    """"""

    def __init__(self,
        *,
        creative_id: builtins.int = ...,
        creative_type: builtins.int = ...,
        card_type: builtins.int = ...,
        creative_content: typing.Optional[global___CreativeContent] = ...,
        ad_cb: typing.Text = ...,
        resource: builtins.int = ...,
        source: builtins.int = ...,
        request_id: typing.Text = ...,
        is_ad: builtins.bool = ...,
        cm_mark: builtins.int = ...,
        index: builtins.int = ...,
        is_ad_loc: builtins.bool = ...,
        card_index: builtins.int = ...,
        client_ip: typing.Text = ...,
        extra: builtins.bytes = ...,
        creative_style: builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["creative_content",b"creative_content"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["ad_cb",b"ad_cb","card_index",b"card_index","card_type",b"card_type","client_ip",b"client_ip","cm_mark",b"cm_mark","creative_content",b"creative_content","creative_id",b"creative_id","creative_style",b"creative_style","creative_type",b"creative_type","extra",b"extra","index",b"index","is_ad",b"is_ad","is_ad_loc",b"is_ad_loc","request_id",b"request_id","resource",b"resource","source",b"source"]) -> None: ...
global___AdInfo = AdInfo

class CreativeContent(google.protobuf.message.Message):
    """"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    VIDEO_ID_FIELD_NUMBER: builtins.int
    USERNAME_FIELD_NUMBER: builtins.int
    IMAGE_URL_FIELD_NUMBER: builtins.int
    IMAGE_MD5_FIELD_NUMBER: builtins.int
    LOG_URL_FIELD_NUMBER: builtins.int
    LOG_MD5_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    CLICK_URL_FIELD_NUMBER: builtins.int
    SHOW_URL_FIELD_NUMBER: builtins.int
    title: typing.Text
    """"""

    description: typing.Text
    """"""

    video_id: builtins.int
    """"""

    username: typing.Text
    """"""

    image_url: typing.Text
    """"""

    image_md5: typing.Text
    """"""

    log_url: typing.Text
    """"""

    log_md5: typing.Text
    """"""

    url: typing.Text
    """"""

    click_url: typing.Text
    """"""

    show_url: typing.Text
    """"""

    def __init__(self,
        *,
        title: typing.Text = ...,
        description: typing.Text = ...,
        video_id: builtins.int = ...,
        username: typing.Text = ...,
        image_url: typing.Text = ...,
        image_md5: typing.Text = ...,
        log_url: typing.Text = ...,
        log_md5: typing.Text = ...,
        url: typing.Text = ...,
        click_url: typing.Text = ...,
        show_url: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["click_url",b"click_url","description",b"description","image_md5",b"image_md5","image_url",b"image_url","log_md5",b"log_md5","log_url",b"log_url","show_url",b"show_url","title",b"title","url",b"url","username",b"username","video_id",b"video_id"]) -> None: ...
global___CreativeContent = CreativeContent
