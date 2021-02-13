from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class AddResponse(BaseResponse):
	response: Optional["AddResponseModel"] = None


class DocUploadResponse(BaseResponse):
	response: Optional["DocUploadResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetTypesResponse(BaseResponse):
	response: Optional["GetTypesResponseModel"] = None


class GetUploadServer(BaseResponse):
	response: Optional["GetUploadServerModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class SaveResponse(BaseResponse):
	response: Optional["SaveResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


AddResponseModelModel = None


class DocUploadResponseModel(BaseResponse):
	file: Optional[str] = None


GetByIdResponseModelModel = array


class GetTypesResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


GetUploadServerModelModel = None


class GetResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None


class SaveResponseModel(BaseResponse):
	type = None
	audio_message = None
	doc = None
	graffiti = None


class SearchResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional["Array"] = None

AddResponse.update_forward_refs()
DocUploadResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetTypesResponse.update_forward_refs()
GetUploadServer.update_forward_refs()
GetResponse.update_forward_refs()
SaveResponse.update_forward_refs()
SearchResponse.update_forward_refs()
