# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/dynamic/common/dynamic.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilireq.grpc.protos.bilibili.app.dynamic.v2 import dynamic_pb2 as bilibili_dot_app_dot_dynamic_dot_v2_dot_dynamic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%bilibili/dynamic/common/dynamic.proto\x12\x10\x62ilibili.dynamic\x1a%bilibili/app/dynamic/v2/dynamic.proto\"y\n\x07\x41tGroup\x12\x31\n\ngroup_type\x18\x01 \x01(\x0e\x32\x1d.bilibili.dynamic.AtGroupType\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\'\n\x05items\x18\x03 \x03(\x0b\x32\x18.bilibili.dynamic.AtItem\"]\n\x06\x41tItem\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61ns\x18\x04 \x01(\x05\x12\x1c\n\x14official_verify_type\x18\x05 \x01(\x05\"\x18\n\tAtListReq\x12\x0b\n\x03uid\x18\x01 \x01(\x03\"6\n\tAtListRsp\x12)\n\x06groups\x18\x01 \x03(\x0b\x32\x19.bilibili.dynamic.AtGroup\"+\n\x0b\x41tSearchReq\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0f\n\x07keyword\x18\x02 \x01(\t\"+\n\x0e\x42ottomBusiness\x12\x0b\n\x03rid\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\x03\"f\n\x0e\x43reateActivity\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\x03\x12\x16\n\x0e\x61\x63tivity_state\x18\x02 \x01(\x05\x12\x17\n\x0fis_new_activity\x18\x03 \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\x04 \x01(\x05\"\x83\x01\n\x10\x43reateAttachCard\x12\x30\n\x05goods\x18\x01 \x01(\x0b\x32!.bilibili.dynamic.CreateGoodsCard\x12=\n\x0b\x63ommon_card\x18\x02 \x01(\x0b\x32(.bilibili.dynamic.CreateCommonAttachCard\"\x98\x02\n\x0f\x43reateCheckResp\x12\x31\n\x07setting\x18\x01 \x01(\x0b\x32 .bilibili.dynamic.PublishSetting\x12\x32\n\npermission\x18\x02 \x01(\x0b\x32\x1e.bilibili.dynamic.UpPermission\x12\x32\n\nshare_info\x18\x03 \x01(\x0b\x32\x1e.bilibili.dynamic.ShareChannel\x12\x36\n\nyellow_bar\x18\x04 \x01(\x0b\x32\".bilibili.dynamic.PublishYellowBar\x12\x32\n\x0cplus_red_dot\x18\x05 \x01(\x0b\x32\x1c.bilibili.dynamic.PlusRedDot\"\x89\x01\n\x16\x43reateCommonAttachCard\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .bilibili.dynamic.AttachCardType\x12\x0e\n\x06\x62iz_id\x18\x02 \x01(\x03\x12\x16\n\x0ereserve_source\x18\x03 \x01(\x05\x12\x17\n\x0freserve_lottery\x18\x04 \x01(\x05\"F\n\rCreateContent\x12\x35\n\x08\x63ontents\x18\x01 \x03(\x0b\x32#.bilibili.dynamic.CreateContentItem\"\x91\x01\n\x11\x43reateContentItem\x12\x10\n\x08raw_text\x18\x01 \x01(\t\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x1d.bilibili.dynamic.ContentType\x12\x0e\n\x06\x62iz_id\x18\x03 \x01(\t\x12-\n\x05goods\x18\x04 \x01(\x0b\x32\x1e.bilibili.dynamic.GoodsContent\"\x8a\x05\n\x0e\x43reateDynVideo\x12\x15\n\rrelation_from\x18\x01 \x01(\t\x12\x10\n\x08\x62iz_from\x18\x03 \x01(\x05\x12\x11\n\tcopyright\x18\x04 \x01(\x05\x12\x11\n\tno_public\x18\x05 \x01(\x05\x12\x12\n\nno_reprint\x18\x06 \x01(\x05\x12\x0e\n\x06source\x18\x07 \x01(\t\x12\r\n\x05\x63over\x18\x08 \x01(\t\x12\r\n\x05title\x18\t \x01(\t\x12\x0b\n\x03tid\x18\n \x01(\x03\x12\x0b\n\x03tag\x18\x0b \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x0c \x01(\t\x12\x16\n\x0e\x64\x65sc_format_id\x18\r \x01(\x03\x12\x11\n\topen_elec\x18\x0e \x01(\x05\x12\r\n\x05\x64time\x18\x0f \x01(\x05\x12\x30\n\x06videos\x18\x10 \x03(\x0b\x32 .bilibili.dynamic.DynVideoMultiP\x12\x36\n\twatermark\x18\x11 \x01(\x0b\x32#.bilibili.dynamic.DynVideoWatermark\x12\x12\n\nmission_id\x18\x12 \x01(\x03\x12\x0f\n\x07\x64ynamic\x18\x13 \x01(\t\x12\x19\n\x11\x64ynamic_extension\x18\x14 \x01(\t\x12\x14\n\x0c\x64ynamic_ctrl\x18\x15 \x01(\t\x12\x14\n\x0c\x64ynamic_from\x18\x16 \x01(\t\x12\x12\n\nlottery_id\x18\x17 \x01(\x03\x12,\n\x04vote\x18\x18 \x01(\x0b\x32\x1e.bilibili.dynamic.DynVideoVote\x12\x1a\n\x12up_selection_reply\x18\x19 \x01(\x08\x12\x16\n\x0eup_close_reply\x18\x1a \x01(\x08\x12\x16\n\x0eup_close_danmu\x18\x1b \x01(\x08\x12\x0f\n\x07up_from\x18\x1c \x01(\x03\x12\x10\n\x08\x64uration\x18\x1d \x01(\x03\"\xb2\x01\n\x14\x43reateDynVideoResult\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x43\n\x10submitact_banner\x18\x03 \x01(\x0b\x32).bilibili.dynamic.DynVideoSubmitActBanner\x12\x37\n\npush_intro\x18\x04 \x01(\x0b\x32#.bilibili.dynamic.DynVideoPushIntro\"\"\n\x0f\x43reateGoodsCard\x12\x0f\n\x07item_id\x18\x01 \x03(\t\"\xf4\x01\n\x0c\x43reateOption\x12\x19\n\x11up_choose_comment\x18\x01 \x01(\x05\x12\x15\n\rclose_comment\x18\x02 \x01(\x05\x12\x14\n\x0c\x66old_exclude\x18\x03 \x01(\x05\x12\x13\n\x0b\x61udit_level\x18\x04 \x01(\x05\x12\x17\n\x0fsync_to_comment\x18\x05 \x01(\x05\x12:\n\x10video_share_info\x18\x06 \x01(\x0b\x32 .bilibili.dynamic.VideoShareInfo\x12\x32\n\x08\x61\x63tivity\x18\x07 \x01(\x0b\x32 .bilibili.dynamic.CreateActivity\"\x87\x01\n\tCreatePic\x12\x0f\n\x07img_src\x18\x01 \x01(\t\x12\x11\n\timg_width\x18\x02 \x01(\x01\x12\x12\n\nimg_height\x18\x03 \x01(\x01\x12\x10\n\x08img_size\x18\x04 \x01(\x01\x12\x30\n\x08img_tags\x18\x05 \x03(\x0b\x32\x1e.bilibili.dynamic.CreatePicTag\"\xea\x01\n\x0c\x43reatePicTag\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\x12\x0b\n\x03tid\x18\x02 \x01(\x03\x12\x0b\n\x03mid\x18\x03 \x01(\x03\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x13\n\x0btext_string\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\x03\x12\x13\n\x0bsource_type\x18\x07 \x01(\x03\x12\x0b\n\x03url\x18\x08 \x01(\t\x12\x12\n\nschema_url\x18\t \x01(\t\x12\x10\n\x08jump_url\x18\n \x01(\t\x12\x13\n\x0borientation\x18\x0b \x01(\x03\x12\t\n\x01x\x18\x0c \x01(\x03\x12\t\n\x01y\x18\r \x01(\x03\x12\x0b\n\x03poi\x18\x0e \x01(\t\"\xca\x01\n\nCreateResp\x12\x0e\n\x06\x64yn_id\x18\x01 \x01(\x03\x12\x12\n\ndyn_id_str\x18\x02 \x01(\t\x12\x10\n\x08\x64yn_type\x18\x03 \x01(\x03\x12\x0f\n\x07\x64yn_rid\x18\x04 \x01(\x03\x12\x37\n\tfake_card\x18\x05 \x01(\x0b\x32$.bilibili.app.dynamic.v2.DynamicItem\x12<\n\x0cvideo_result\x18\x06 \x01(\x0b\x32&.bilibili.dynamic.CreateDynVideoResult\"\x9b\x01\n\tCreateTag\x12%\n\x03lbs\x18\x01 \x01(\x0b\x32\x18.bilibili.dynamic.ExtLbs\x12\x32\n\x08sdk_game\x18\x02 \x01(\x0b\x32 .bilibili.dynamic.BottomBusiness\x12\x33\n\tdiversion\x18\x03 \x01(\x0b\x32 .bilibili.dynamic.BottomBusiness\"\'\n\x0b\x43reateTopic\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\"K\n\x0b\x44ynIdentity\x12\x0e\n\x06\x64yn_id\x18\x01 \x01(\x03\x12,\n\x07revs_id\x18\x02 \x01(\x0b\x32\x1b.bilibili.dynamic.DynRevsId\"*\n\tDynRevsId\x12\x10\n\x08\x64yn_type\x18\x01 \x01(\x03\x12\x0b\n\x03rid\x18\x02 \x01(\x03\"\x89\x06\n\x0e\x44ynVideoEditor\x12\x0b\n\x03\x63id\x18\x01 \x01(\x03\x12\x0e\n\x06upfrom\x18\x02 \x01(\x05\x12\x0f\n\x07\x66ilters\x18\x03 \x01(\t\x12\r\n\x05\x66onts\x18\x04 \x01(\t\x12\x11\n\tsubtitles\x18\x05 \x01(\t\x12\x0c\n\x04\x62gms\x18\x06 \x01(\t\x12\x10\n\x08stickers\x18\x07 \x01(\t\x12\x18\n\x10videoup_stickers\x18\x08 \x01(\t\x12\r\n\x05trans\x18\t \x01(\t\x12\x0f\n\x07makeups\x18\n \x01(\t\x12\x10\n\x08surgerys\x18\x0b \x01(\t\x12\x10\n\x08videofxs\x18\x0c \x01(\t\x12\x0e\n\x06themes\x18\r \x01(\t\x12\x12\n\ncooperates\x18\x0e \x01(\t\x12\x0f\n\x07rhythms\x18\x0f \x01(\t\x12\x0f\n\x07\x65\x66\x66\x65\x63ts\x18\x10 \x01(\t\x12\x13\n\x0b\x62\x61\x63kgrounds\x18\x11 \x01(\t\x12\x0e\n\x06videos\x18\x12 \x01(\t\x12\x0e\n\x06sounds\x18\x13 \x01(\t\x12\x0f\n\x07\x66lowers\x18\x14 \x01(\t\x12\x17\n\x0f\x63over_templates\x18\x15 \x01(\t\x12\x0b\n\x03tts\x18\x16 \x01(\t\x12\x10\n\x08openings\x18\x17 \x01(\t\x12\x13\n\x0brecord_text\x18\x18 \x01(\x08\x12\x0e\n\x06vupers\x18\x19 \x01(\t\x12\x10\n\x08\x66\x65\x61tures\x18\x1a \x01(\t\x12\x15\n\rbcut_features\x18\x1b \x01(\t\x12\x14\n\x0c\x61udio_record\x18\x1c \x01(\x05\x12\x0e\n\x06\x63\x61mera\x18\x1d \x01(\x05\x12\r\n\x05speed\x18\x1e \x01(\x05\x12\x15\n\rcamera_rotate\x18\x1f \x01(\x05\x12\x15\n\rscreen_record\x18  \x01(\x05\x12\x13\n\x0b\x64\x65\x66\x61ult_end\x18! \x01(\x05\x12\x10\n\x08\x64uration\x18\" \x01(\x05\x12\x11\n\tpic_count\x18# \x01(\x05\x12\x13\n\x0bvideo_count\x18$ \x01(\x05\x12\x15\n\rshot_duration\x18% \x01(\x05\x12\x11\n\tshot_game\x18& \x01(\t\x12\x11\n\thighlight\x18\' \x01(\x08\x12\x15\n\rhighlight_cnt\x18( \x01(\x05\x12\x11\n\tpip_count\x18) \x01(\x05\"t\n\x0e\x44ynVideoHotAct\x12\x0e\n\x06\x61\x63t_id\x18\x01 \x01(\x03\x12\r\n\x05\x65time\x18\x02 \x01(\x03\x12\n\n\x02id\x18\x03 \x01(\x03\x12\x0b\n\x03pic\x18\x04 \x01(\t\x12\r\n\x05stime\x18\x05 \x01(\x03\x12\r\n\x05title\x18\x06 \x01(\t\x12\x0c\n\x04link\x18\x07 \x01(\t\"p\n\x0e\x44ynVideoMultiP\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0b\n\x03\x63id\x18\x03 \x01(\x03\x12\x30\n\x06\x65\x64itor\x18\x04 \x01(\x0b\x32 .bilibili.dynamic.DynVideoEditor\"/\n\x11\x44ynVideoPushIntro\x12\x0c\n\x04show\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\"r\n\x17\x44ynVideoSubmitActBanner\x12\x13\n\x0bhotact_text\x18\x01 \x01(\t\x12\x12\n\nhotact_url\x18\x02 \x01(\t\x12.\n\x04list\x18\x03 \x03(\x0b\x32 .bilibili.dynamic.DynVideoHotAct\"J\n\x0c\x44ynVideoVote\x12\x0f\n\x07vote_id\x18\x01 \x01(\x03\x12\x12\n\nvote_title\x18\x02 \x01(\t\x12\x15\n\rtop_for_reply\x18\x03 \x01(\x05\"B\n\x11\x44ynVideoWatermark\x12\r\n\x05state\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x10\n\x08position\x18\x03 \x01(\x05\"\xac\x01\n\x06\x45xtLbs\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x10\n\x08\x64istance\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x03\x12\x0b\n\x03poi\x18\x04 \x01(\t\x12*\n\x08location\x18\x05 \x01(\x0b\x32\x18.bilibili.dynamic.LbsLoc\x12\x12\n\nshow_title\x18\x06 \x01(\t\x12\r\n\x05title\x18\x07 \x01(\t\x12\x15\n\rshow_distance\x18\x08 \x01(\t\" \n\x0fGetUidByNameReq\x12\r\n\x05names\x18\x01 \x03(\t\"y\n\x0fGetUidByNameRsp\x12\x39\n\x04uids\x18\x01 \x03(\x0b\x32+.bilibili.dynamic.GetUidByNameRsp.UidsEntry\x1a+\n\tUidsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"E\n\x0cGoodsContent\x12\x13\n\x0bsource_type\x18\x01 \x01(\x05\x12\x0f\n\x07item_id\x18\x02 \x01(\x03\x12\x0f\n\x07shop_id\x18\x03 \x01(\x03\"\xa3\x01\n\x10LaunchedActivity\x12\x14\n\x0cmodule_title\x18\x01 \x01(\t\x12:\n\nactivities\x18\x02 \x03(\x0b\x32&.bilibili.dynamic.LaunchedActivityItem\x12=\n\tshow_more\x18\x03 \x01(\x0b\x32*.bilibili.dynamic.ShowMoreLaunchedActivity\"Z\n\x14LaunchedActivityItem\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\x03\x12\x15\n\ractivity_name\x18\x02 \x01(\t\x12\x16\n\x0e\x61\x63tivity_state\x18\x03 \x01(\x05\"\"\n\x06LbsLoc\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lng\x18\x02 \x01(\x01\"\xed\x01\n\x0cMetaDataCtrl\x12\x10\n\x08platform\x18\x01 \x01(\t\x12\r\n\x05\x62uild\x18\x02 \x01(\t\x12\x10\n\x08mobi_app\x18\x03 \x01(\t\x12\r\n\x05\x62uvid\x18\x04 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x05 \x01(\t\x12\x12\n\nfrom_spmid\x18\x06 \x01(\t\x12\x0c\n\x04\x66rom\x18\x07 \x01(\t\x12\x10\n\x08trace_id\x18\x08 \x01(\t\x12\x15\n\rteenager_mode\x18\t \x01(\x05\x12\x12\n\ncold_start\x18\n \x01(\x05\x12\x0f\n\x07version\x18\x0b \x01(\t\x12\x0f\n\x07network\x18\x0c \x01(\x05\x12\n\n\x02ip\x18\r \x01(\t\"&\n\nPlusRedDot\x12\x18\n\x10plus_has_red_dot\x18\x01 \x01(\x03\"\x80\x01\n\x07Program\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\r\n\x05\x63over\x18\x03 \x01(\t\x12\x12\n\ntarget_url\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x14\n\x0cprogram_text\x18\x06 \x01(\t\x12\x11\n\tjump_text\x18\x07 \x01(\t\"a\n\x0ePublishSetting\x12\x1c\n\x14min_words_to_article\x18\x01 \x01(\x05\x12\x1c\n\x14max_words_to_article\x18\x02 \x01(\x05\x12\x13\n\x0bupload_size\x18\x03 \x01(\x05\";\n\x10PublishYellowBar\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\"j\n\x0fRepostInitCheck\x12\x31\n\nrepost_src\x18\x01 \x01(\x0b\x32\x1d.bilibili.dynamic.DynIdentity\x12\x10\n\x08share_id\x18\x02 \x01(\t\x12\x12\n\nshare_mode\x18\x03 \x01(\x05\"z\n\x0cShareChannel\x12\x14\n\x0cshare_origin\x18\x01 \x01(\t\x12\x0b\n\x03oid\x18\x02 \x01(\t\x12\x0b\n\x03sid\x18\x03 \x01(\t\x12:\n\x0eshare_channels\x18\x04 \x03(\x0b\x32\".bilibili.dynamic.ShareChannelItem\"y\n\x10ShareChannelItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07picture\x18\x02 \x01(\t\x12\x15\n\rshare_channel\x18\x03 \x01(\t\x12/\n\x07reserve\x18\x04 \x01(\x0b\x32\x1e.bilibili.dynamic.ShareReserve\"\xfe\x01\n\x0cShareReserve\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x14\n\x0cqr_code_icon\x18\x03 \x01(\t\x12\x14\n\x0cqr_code_text\x18\x04 \x01(\t\x12\x13\n\x0bqr_code_url\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x07 \x01(\t\x12\x34\n\x06poster\x18\x08 \x01(\x0b\x32$.bilibili.dynamic.ShareReservePoster\x12>\n\x0freserve_lottery\x18\t \x01(\x0b\x32%.bilibili.dynamic.ShareReserveLottery\"1\n\x13ShareReserveLottery\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"@\n\x12ShareReservePoster\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x01\x12\x0e\n\x06height\x18\x03 \x01(\x01\"2\n\x0bShareResult\x12\x14\n\x0cshare_enable\x18\x01 \x01(\x03\x12\r\n\x05toast\x18\x02 \x01(\t\"A\n\x18ShowMoreLaunchedActivity\x12\x13\n\x0b\x62utton_text\x18\x01 \x01(\t\x12\x10\n\x08jump_url\x18\x02 \x01(\t\"\x81\x01\n\x06Sketch\x12\r\n\x05title\x18\x01 \x01(\t\x12\x11\n\tdesc_text\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x0e\n\x06\x62iz_id\x18\x04 \x01(\x03\x12\x10\n\x08\x62iz_type\x18\x05 \x01(\x03\x12\x11\n\tcover_url\x18\x06 \x01(\t\x12\x12\n\ntarget_url\x18\x07 \x01(\t\"\xb5\x01\n\x0cUpPermission\x12\x31\n\x05items\x18\x01 \x03(\x0b\x32\".bilibili.dynamic.UpPermissionItem\x12=\n\x11launched_activity\x18\x02 \x01(\x0b\x32\".bilibili.dynamic.LaunchedActivity\x12\x33\n\x0cshare_result\x18\x03 \x01(\x0b\x32\x1d.bilibili.dynamic.ShareResult\"\x99\x01\n\x10UpPermissionItem\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x12\n\npermission\x18\x02 \x01(\x05\x12\r\n\x05title\x18\x03 \x01(\t\x12\x10\n\x08subtitle\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x10\n\x08jump_url\x18\x06 \x01(\t\x12\r\n\x05toast\x18\x07 \x01(\t\x12\x13\n\x0bhas_red_dot\x18\x08 \x01(\x03\"~\n\x0eUserCreateMeta\x12\x30\n\x08\x61pp_meta\x18\x01 \x01(\x0b\x32\x1e.bilibili.dynamic.MetaDataCtrl\x12%\n\x03loc\x18\x02 \x01(\x0b\x32\x18.bilibili.dynamic.LbsLoc\x12\x13\n\x0brepost_mode\x18\x03 \x01(\x05\"+\n\x0eVideoShareInfo\x12\x0b\n\x03\x63id\x18\x01 \x01(\x03\x12\x0c\n\x04part\x18\x02 \x01(\x05*\x8e\x01\n\x0b\x41tGroupType\x12\x19\n\x15\x41T_GROUP_TYPE_DEFAULT\x10\x00\x12\x18\n\x14\x41T_GROUP_TYPE_RECENT\x10\x01\x12\x18\n\x14\x41T_GROUP_TYPE_FOLLOW\x10\x02\x12\x16\n\x12\x41T_GROUP_TYPE_FANS\x10\x03\x12\x18\n\x14\x41T_GROUP_TYPE_OTHERS\x10\x04*\x94\x03\n\x0e\x41ttachCardType\x12\x14\n\x10\x41TTACH_CARD_NONE\x10\x00\x12\x15\n\x11\x41TTACH_CARD_GOODS\x10\x01\x12\x14\n\x10\x41TTACH_CARD_VOTE\x10\x02\x12\x13\n\x0f\x41TTACH_CARD_UGC\x10\x03\x12\x18\n\x14\x41TTACH_CARD_ACTIVITY\x10\x04\x12!\n\x1d\x41TTACH_CARD_OFFICIAL_ACTIVITY\x10\x05\x12\x15\n\x11\x41TTACH_CARD_TOPIC\x10\x06\x12\x13\n\x0f\x41TTACH_CARD_OGV\x10\x07\x12\x18\n\x14\x41TTACH_CARD_AUTO_OGV\x10\x08\x12\x14\n\x10\x41TTACH_CARD_GAME\x10\t\x12\x15\n\x11\x41TTACH_CARD_MANGA\x10\n\x12\x1a\n\x16\x41TTACH_CARD_DECORATION\x10\x0b\x12\x15\n\x11\x41TTACH_CARD_MATCH\x10\x0c\x12\x14\n\x10\x41TTACH_CARD_PUGV\x10\r\x12\x17\n\x13\x41TTACH_CARD_RESERVE\x10\x0e\x12\x18\n\x14\x41TTACH_CARD_UP_TOPIC\x10\x0f*\xd3\x01\n\x0b\x43ontentType\x12\x15\n\x11\x43ONTENT_TYPE_NONE\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\x06\n\x02\x41T\x10\x02\x12\x0b\n\x07LOTTERY\x10\x03\x12\x08\n\x04VOTE\x10\x04\x12\t\n\x05TOPIC\x10\x05\x12\t\n\x05GOODS\x10\x06\x12\x06\n\x02\x42V\x10\x07\x12\x06\n\x02\x41V\x10\x08\x12\t\n\x05\x45MOJI\x10\t\x12\x08\n\x04USER\x10\n\x12\x06\n\x02\x43V\x10\x0b\x12\x06\n\x02VC\x10\x0c\x12\x07\n\x03WEB\x10\r\x12\n\n\x06TAOBAO\x10\x0e\x12\x08\n\x04MAIL\x10\x0f\x12\x0e\n\nOGV_SEASON\x10\x10\x12\n\n\x06OGV_EP\x10\x11*\xd1\x01\n\x14\x43reateInitCheckScene\x12#\n\x1f\x43REATE_INIT_CHECK_SCENE_INVALID\x10\x00\x12\"\n\x1e\x43REATE_INIT_CHECK_SCENE_NORMAL\x10\x01\x12\"\n\x1e\x43REATE_INIT_CHECK_SCENE_REPOST\x10\x02\x12!\n\x1d\x43REATE_INIT_CHECK_SCENE_SHARE\x10\x03\x12)\n%CREATE_INIT_CHECK_SCENE_RESERVE_SHARE\x10\x04*\xbd\x02\n\x0b\x43reateScene\x12\x18\n\x14\x43REATE_SCENE_INVALID\x10\x00\x12\x1c\n\x18\x43REATE_SCENE_CREATE_WORD\x10\x01\x12\x1c\n\x18\x43REATE_SCENE_CREATE_DRAW\x10\x02\x12!\n\x1d\x43REATE_SCENE_CREATE_DYN_VIDEO\x10\x03\x12\x17\n\x13\x43REATE_SCENE_REPOST\x10\x04\x12\x1a\n\x16\x43REATE_SCENE_SHARE_BIZ\x10\x05\x12\x1b\n\x17\x43REATE_SCENE_SHARE_PAGE\x10\x06\x12\x1e\n\x1a\x43REATE_SCENE_SHARE_PROGRAM\x10\x07\x12\x1b\n\x17\x43REATE_SCENE_REPLY_SYNC\x10\x08\x12&\n\"CREATE_SCENE_REPLY_CREATE_ACTIVITY\x10\t*F\n\rReserveSource\x12\x16\n\x12RESERVE_SOURCE_NEW\x10\x00\x12\x1d\n\x19RESERVE_SOURCE_ASSOCIATED\x10\x01*\x88\x03\n\x10UpPermissionType\x12\x1b\n\x17UP_PERMISSION_TYPE_NONE\x10\x00\x12\x1e\n\x1aUP_PERMISSION_TYPE_LOTTERY\x10\x01\x12%\n!UP_PERMISSION_TYPE_CLIP_PUBLISHED\x10\x02\x12&\n\"UP_PERMISSION_TYPE_UGC_ATTACH_CARD\x10\x03\x12(\n$UP_PERMISSION_TYPE_GOODS_ATTACH_CARD\x10\x04\x12%\n!UP_PERMISSION_TYPE_CHOOSE_COMMENT\x10\x05\x12&\n\"UP_PERMISSION_TYPE_CONTROL_COMMENT\x10\x06\x12$\n UP_PERMISSION_TYPE_CONTROL_DANMU\x10\x07\x12$\n UP_PERMISSION_TYPE_VIDEO_RESERVE\x10\x08\x12#\n\x1fUP_PERMISSION_TYPE_LIVE_RESERVE\x10\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.dynamic.common.dynamic_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETUIDBYNAMERSP_UIDSENTRY._options = None
  _GETUIDBYNAMERSP_UIDSENTRY._serialized_options = b'8\001'
  _ATGROUPTYPE._serialized_start=7469
  _ATGROUPTYPE._serialized_end=7611
  _ATTACHCARDTYPE._serialized_start=7614
  _ATTACHCARDTYPE._serialized_end=8018
  _CONTENTTYPE._serialized_start=8021
  _CONTENTTYPE._serialized_end=8232
  _CREATEINITCHECKSCENE._serialized_start=8235
  _CREATEINITCHECKSCENE._serialized_end=8444
  _CREATESCENE._serialized_start=8447
  _CREATESCENE._serialized_end=8764
  _RESERVESOURCE._serialized_start=8766
  _RESERVESOURCE._serialized_end=8836
  _UPPERMISSIONTYPE._serialized_start=8839
  _UPPERMISSIONTYPE._serialized_end=9231
  _ATGROUP._serialized_start=98
  _ATGROUP._serialized_end=219
  _ATITEM._serialized_start=221
  _ATITEM._serialized_end=314
  _ATLISTREQ._serialized_start=316
  _ATLISTREQ._serialized_end=340
  _ATLISTRSP._serialized_start=342
  _ATLISTRSP._serialized_end=396
  _ATSEARCHREQ._serialized_start=398
  _ATSEARCHREQ._serialized_end=441
  _BOTTOMBUSINESS._serialized_start=443
  _BOTTOMBUSINESS._serialized_end=486
  _CREATEACTIVITY._serialized_start=488
  _CREATEACTIVITY._serialized_end=590
  _CREATEATTACHCARD._serialized_start=593
  _CREATEATTACHCARD._serialized_end=724
  _CREATECHECKRESP._serialized_start=727
  _CREATECHECKRESP._serialized_end=1007
  _CREATECOMMONATTACHCARD._serialized_start=1010
  _CREATECOMMONATTACHCARD._serialized_end=1147
  _CREATECONTENT._serialized_start=1149
  _CREATECONTENT._serialized_end=1219
  _CREATECONTENTITEM._serialized_start=1222
  _CREATECONTENTITEM._serialized_end=1367
  _CREATEDYNVIDEO._serialized_start=1370
  _CREATEDYNVIDEO._serialized_end=2020
  _CREATEDYNVIDEORESULT._serialized_start=2023
  _CREATEDYNVIDEORESULT._serialized_end=2201
  _CREATEGOODSCARD._serialized_start=2203
  _CREATEGOODSCARD._serialized_end=2237
  _CREATEOPTION._serialized_start=2240
  _CREATEOPTION._serialized_end=2484
  _CREATEPIC._serialized_start=2487
  _CREATEPIC._serialized_end=2622
  _CREATEPICTAG._serialized_start=2625
  _CREATEPICTAG._serialized_end=2859
  _CREATERESP._serialized_start=2862
  _CREATERESP._serialized_end=3064
  _CREATETAG._serialized_start=3067
  _CREATETAG._serialized_end=3222
  _CREATETOPIC._serialized_start=3224
  _CREATETOPIC._serialized_end=3263
  _DYNIDENTITY._serialized_start=3265
  _DYNIDENTITY._serialized_end=3340
  _DYNREVSID._serialized_start=3342
  _DYNREVSID._serialized_end=3384
  _DYNVIDEOEDITOR._serialized_start=3387
  _DYNVIDEOEDITOR._serialized_end=4164
  _DYNVIDEOHOTACT._serialized_start=4166
  _DYNVIDEOHOTACT._serialized_end=4282
  _DYNVIDEOMULTIP._serialized_start=4284
  _DYNVIDEOMULTIP._serialized_end=4396
  _DYNVIDEOPUSHINTRO._serialized_start=4398
  _DYNVIDEOPUSHINTRO._serialized_end=4445
  _DYNVIDEOSUBMITACTBANNER._serialized_start=4447
  _DYNVIDEOSUBMITACTBANNER._serialized_end=4561
  _DYNVIDEOVOTE._serialized_start=4563
  _DYNVIDEOVOTE._serialized_end=4637
  _DYNVIDEOWATERMARK._serialized_start=4639
  _DYNVIDEOWATERMARK._serialized_end=4705
  _EXTLBS._serialized_start=4708
  _EXTLBS._serialized_end=4880
  _GETUIDBYNAMEREQ._serialized_start=4882
  _GETUIDBYNAMEREQ._serialized_end=4914
  _GETUIDBYNAMERSP._serialized_start=4916
  _GETUIDBYNAMERSP._serialized_end=5037
  _GETUIDBYNAMERSP_UIDSENTRY._serialized_start=4994
  _GETUIDBYNAMERSP_UIDSENTRY._serialized_end=5037
  _GOODSCONTENT._serialized_start=5039
  _GOODSCONTENT._serialized_end=5108
  _LAUNCHEDACTIVITY._serialized_start=5111
  _LAUNCHEDACTIVITY._serialized_end=5274
  _LAUNCHEDACTIVITYITEM._serialized_start=5276
  _LAUNCHEDACTIVITYITEM._serialized_end=5366
  _LBSLOC._serialized_start=5368
  _LBSLOC._serialized_end=5402
  _METADATACTRL._serialized_start=5405
  _METADATACTRL._serialized_end=5642
  _PLUSREDDOT._serialized_start=5644
  _PLUSREDDOT._serialized_end=5682
  _PROGRAM._serialized_start=5685
  _PROGRAM._serialized_end=5813
  _PUBLISHSETTING._serialized_start=5815
  _PUBLISHSETTING._serialized_end=5912
  _PUBLISHYELLOWBAR._serialized_start=5914
  _PUBLISHYELLOWBAR._serialized_end=5973
  _REPOSTINITCHECK._serialized_start=5975
  _REPOSTINITCHECK._serialized_end=6081
  _SHARECHANNEL._serialized_start=6083
  _SHARECHANNEL._serialized_end=6205
  _SHARECHANNELITEM._serialized_start=6207
  _SHARECHANNELITEM._serialized_end=6328
  _SHARERESERVE._serialized_start=6331
  _SHARERESERVE._serialized_end=6585
  _SHARERESERVELOTTERY._serialized_start=6587
  _SHARERESERVELOTTERY._serialized_end=6636
  _SHARERESERVEPOSTER._serialized_start=6638
  _SHARERESERVEPOSTER._serialized_end=6702
  _SHARERESULT._serialized_start=6704
  _SHARERESULT._serialized_end=6754
  _SHOWMORELAUNCHEDACTIVITY._serialized_start=6756
  _SHOWMORELAUNCHEDACTIVITY._serialized_end=6821
  _SKETCH._serialized_start=6824
  _SKETCH._serialized_end=6953
  _UPPERMISSION._serialized_start=6956
  _UPPERMISSION._serialized_end=7137
  _UPPERMISSIONITEM._serialized_start=7140
  _UPPERMISSIONITEM._serialized_end=7293
  _USERCREATEMETA._serialized_start=7295
  _USERCREATEMETA._serialized_end=7421
  _VIDEOSHAREINFO._serialized_start=7423
  _VIDEOSHAREINFO._serialized_end=7466
# @@protoc_insertion_point(module_scope)
