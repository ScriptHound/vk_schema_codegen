from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class CopyResponse(BaseResponse):
	response: Optional["CopyResponseModel"] = None


class CreateAlbumResponse(BaseResponse):
	response: Optional["CreateAlbumResponseModel"] = None


class CreateCommentResponse(BaseResponse):
	response: Optional["CreateCommentResponseModel"] = None


class DeleteCommentResponse(BaseResponse):
	response: Optional["DeleteCommentResponseModel"] = None


class GetAlbumsCountResponse(BaseResponse):
	response: Optional["GetAlbumsCountResponseModel"] = None


class GetAlbumsResponse(BaseResponse):
	response: Optional["GetAlbumsResponseModel"] = None


class GetAllCommentsResponse(BaseResponse):
	response: Optional["GetAllCommentsResponseModel"] = None


class GetAllExtendedResponse(BaseResponse):
	response: Optional["GetAllExtendedResponseModel"] = None


class GetAllResponse(BaseResponse):
	response: Optional["GetAllResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
	response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
	response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
	response: Optional["GetCommentsResponseModel"] = None


class GetMarketUploadServerResponse(BaseResponse):
	response: Optional["GetMarketUploadServerResponseModel"] = None


class GetMessagesUploadServerResponse(BaseResponse):
	response: Optional["GetMessagesUploadServerResponseModel"] = None


class GetNewTagsResponse(BaseResponse):
	response: Optional["GetNewTagsResponseModel"] = None


class GetTagsResponse(BaseResponse):
	response: Optional["GetTagsResponseModel"] = None


class GetUploadServerResponse(BaseResponse):
	response: Optional["GetUploadServerResponseModel"] = None


class GetUserPhotosExtendedResponse(BaseResponse):
	response: Optional["GetUserPhotosExtendedResponseModel"] = None


class GetUserPhotosResponse(BaseResponse):
	response: Optional["GetUserPhotosResponseModel"] = None


class GetWallUploadServerResponse(BaseResponse):
	response: Optional["GetWallUploadServerResponseModel"] = None


class GetExtendedResponse(BaseResponse):
	response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class MarketAlbumUploadResponse(BaseResponse):
	response: Optional["MarketAlbumUploadResponseModel"] = None


class MarketUploadResponse(BaseResponse):
	response: Optional["MarketUploadResponseModel"] = None


class MessageUploadResponse(BaseResponse):
	response: Optional["MessageUploadResponseModel"] = None


class OwnerCoverUploadResponse(BaseResponse):
	response: Optional["OwnerCoverUploadResponseModel"] = None


class OwnerUploadResponse(BaseResponse):
	response: Optional["OwnerUploadResponseModel"] = None


class PhotoUploadResponse(BaseResponse):
	response: Optional["PhotoUploadResponseModel"] = None


class PutTagResponse(BaseResponse):
	response: Optional["PutTagResponseModel"] = None


class RestoreCommentResponse(BaseResponse):
	response: Optional["RestoreCommentResponseModel"] = None


class SaveMarketAlbumPhotoResponse(BaseResponse):
	response: Optional["SaveMarketAlbumPhotoResponseModel"] = None


class SaveMarketPhotoResponse(BaseResponse):
	response: Optional["SaveMarketPhotoResponseModel"] = None


class SaveMessagesPhotoResponse(BaseResponse):
	response: Optional["SaveMessagesPhotoResponseModel"] = None


class SaveOwnerCoverPhotoResponse(BaseResponse):
	response: Optional["SaveOwnerCoverPhotoResponseModel"] = None


class SaveOwnerPhotoResponse(BaseResponse):
	response: Optional["SaveOwnerPhotoResponseModel"] = None


class SaveWallPhotoResponse(BaseResponse):
	response: Optional["SaveWallPhotoResponseModel"] = None


class SaveResponse(BaseResponse):
	response: Optional["SaveResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


class WallUploadResponse(BaseResponse):
	response: Optional["WallUploadResponseModel"] = None


CopyResponseModel = int


CreateAlbumResponseModel = Optional[Photosphotoalbumfull]


CreateCommentResponseModel = int


DeleteCommentResponseModel = Optional[Baseboolint]


GetAlbumsCountResponseModel = int


class GetAlbumsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetAllCommentsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetAllExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	more: Optional["baseboolint"] = None


class GetAllResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	more: Optional["baseboolint"] = None


GetByIdExtendedResponseModel = List[PhotosPhotoFull]


GetByIdResponseModel = List[PhotosPhoto]


class GetCommentsExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	real_offset: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetCommentsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	real_offset: Optional["integer"] = None
	items: Optional["array"] = None


GetMarketUploadServerResponseModel = Optional[Baseuploadserver]


GetMessagesUploadServerResponseModel = Optional[Photosphotoupload]


class GetNewTagsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


GetTagsResponseModel = List[PhotosPhotoTag]


GetUploadServerResponseModel = Optional[Photosphotoupload]


class GetUserPhotosExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetUserPhotosResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


GetWallUploadServerResponseModel = Optional[Photosphotoupload]


class GetExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class MarketAlbumUploadResponseModel(BaseResponse):
	gid: Optional["integer"] = None
	hash: Optional["string"] = None
	photo: Optional["string"] = None
	server: Optional["integer"] = None


class MarketUploadResponseModel(BaseResponse):
	crop_data: Optional["string"] = None
	crop_hash: Optional["string"] = None
	group_id: Optional["integer"] = None
	hash: Optional["string"] = None
	photo: Optional["string"] = None
	server: Optional["integer"] = None


class MessageUploadResponseModel(BaseResponse):
	hash: Optional["string"] = None
	photo: Optional["string"] = None
	server: Optional["integer"] = None


class OwnerCoverUploadResponseModel(BaseResponse):
	hash: Optional["string"] = None
	photo: Optional["string"] = None


class OwnerUploadResponseModel(BaseResponse):
	hash: Optional["string"] = None
	photo: Optional["string"] = None
	server: Optional["integer"] = None


class PhotoUploadResponseModel(BaseResponse):
	aid: Optional["integer"] = None
	hash: Optional["string"] = None
	photo: Optional["string"] = None
	photos_list: Optional["string"] = None
	server: Optional["integer"] = None


PutTagResponseModel = int


RestoreCommentResponseModel = Optional[Baseboolint]


SaveMarketAlbumPhotoResponseModel = List[PhotosPhoto]


SaveMarketPhotoResponseModel = List[PhotosPhoto]


SaveMessagesPhotoResponseModel = List[PhotosPhoto]


SaveOwnerCoverPhotoResponseModel = List[BaseImage]


class SaveOwnerPhotoResponseModel(BaseResponse):
	photo_hash: Optional["string"] = None
	photo_src: Optional["string"] = None
	photo_src_big: Optional["string"] = None
	photo_src_small: Optional["string"] = None
	saved: Optional["integer"] = None
	post_id: Optional["integer"] = None


SaveWallPhotoResponseModel = List[PhotosPhoto]


SaveResponseModel = List[PhotosPhoto]


class SearchResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class WallUploadResponseModel(BaseResponse):
	hash: Optional["string"] = None
	photo: Optional["string"] = None
	server: Optional["integer"] = None

CopyResponse.update_forward_refs()
CreateAlbumResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
DeleteCommentResponse.update_forward_refs()
GetAlbumsCountResponse.update_forward_refs()
GetAlbumsResponse.update_forward_refs()
GetAllCommentsResponse.update_forward_refs()
GetAllExtendedResponse.update_forward_refs()
GetAllResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetMarketUploadServerResponse.update_forward_refs()
GetMessagesUploadServerResponse.update_forward_refs()
GetNewTagsResponse.update_forward_refs()
GetTagsResponse.update_forward_refs()
GetUploadServerResponse.update_forward_refs()
GetUserPhotosExtendedResponse.update_forward_refs()
GetUserPhotosResponse.update_forward_refs()
GetWallUploadServerResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
MarketAlbumUploadResponse.update_forward_refs()
MarketUploadResponse.update_forward_refs()
MessageUploadResponse.update_forward_refs()
OwnerCoverUploadResponse.update_forward_refs()
OwnerUploadResponse.update_forward_refs()
PhotoUploadResponse.update_forward_refs()
PutTagResponse.update_forward_refs()
RestoreCommentResponse.update_forward_refs()
SaveMarketAlbumPhotoResponse.update_forward_refs()
SaveMarketPhotoResponse.update_forward_refs()
SaveMessagesPhotoResponse.update_forward_refs()
SaveOwnerCoverPhotoResponse.update_forward_refs()
SaveOwnerPhotoResponse.update_forward_refs()
SaveWallPhotoResponse.update_forward_refs()
SaveResponse.update_forward_refs()
SearchResponse.update_forward_refs()
WallUploadResponse.update_forward_refs()
