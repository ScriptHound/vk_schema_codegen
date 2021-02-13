from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse



class AddVoteResponse(BaseResponse):
	response: Optional["AddVoteResponseModel"] = None


class CreateResponse(BaseResponse):
	response: Optional["CreateResponseModel"] = None


class DeleteVoteResponse(BaseResponse):
	response: Optional["DeleteVoteResponseModel"] = None


class GetBackgroundsResponse(BaseResponse):
	response: Optional["GetBackgroundsResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetVotersResponse(BaseResponse):
	response: Optional["GetVotersResponseModel"] = None


class SavePhotoResponse(BaseResponse):
	response: Optional["SavePhotoResponseModel"] = None


AddVoteResponseModelModel = None


CreateResponseModelModel = None


DeleteVoteResponseModelModel = None


GetBackgroundsResponseModelModel = array


GetByIdResponseModelModel = None


GetVotersResponseModelModel = array


SavePhotoResponseModelModel = None

AddVoteResponse.update_forward_refs()
CreateResponse.update_forward_refs()
DeleteVoteResponse.update_forward_refs()
GetBackgroundsResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetVotersResponse.update_forward_refs()
SavePhotoResponse.update_forward_refs()
