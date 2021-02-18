from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class CreateChatResponse(BaseResponse):
	response: Optional["CreateChatResponseModel"] = None


class DeleteChatPhotoResponse(BaseResponse):
	response: Optional["DeleteChatPhotoResponseModel"] = None


class DeleteConversationResponse(BaseResponse):
	response: Optional["DeleteConversationResponseModel"] = None


class DeleteResponse(BaseResponse):
	response: Optional["DeleteResponseModel"] = None


class EditResponse(BaseResponse):
	response: Optional["EditResponseModel"] = None


class GetByConversationMessageIdResponse(BaseResponse):
	response: Optional["GetByConversationMessageIdResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
	response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetChatPreviewResponse(BaseResponse):
	response: Optional["GetChatPreviewResponseModel"] = None


class GetChatChatIdsFieldsResponse(BaseResponse):
	response: Optional["GetChatChatIdsFieldsResponseModel"] = None


class GetChatChatIdsResponse(BaseResponse):
	response: Optional["GetChatChatIdsResponseModel"] = None


class GetChatFieldsResponse(BaseResponse):
	response: Optional["GetChatFieldsResponseModel"] = None


class GetChatResponse(BaseResponse):
	response: Optional["GetChatResponseModel"] = None


class GetConversationMembersResponse(BaseResponse):
	response: Optional["GetConversationMembersResponseModel"] = None


class GetConversationsByIdExtendedResponse(BaseResponse):
	response: Optional["GetConversationsByIdExtendedResponseModel"] = None


class GetConversationsByIdResponse(BaseResponse):
	response: Optional["GetConversationsByIdResponseModel"] = None


class GetConversationsResponse(BaseResponse):
	response: Optional["GetConversationsResponseModel"] = None


class GetHistoryAttachmentsResponse(BaseResponse):
	response: Optional["GetHistoryAttachmentsResponseModel"] = None


class GetHistoryExtendedResponse(BaseResponse):
	response: Optional["GetHistoryExtendedResponseModel"] = None


class GetHistoryResponse(BaseResponse):
	response: Optional["GetHistoryResponseModel"] = None


class GetImportantMessagesExtendedResponse(BaseResponse):
	response: Optional["GetImportantMessagesExtendedResponseModel"] = None


class GetImportantMessagesResponse(BaseResponse):
	response: Optional["GetImportantMessagesResponseModel"] = None


class GetIntentUsersResponse(BaseResponse):
	response: Optional["GetIntentUsersResponseModel"] = None


class GetInviteLinkResponse(BaseResponse):
	response: Optional["GetInviteLinkResponseModel"] = None


class GetLastActivityResponse(BaseResponse):
	response: Optional["GetLastActivityResponseModel"] = None


class GetLongPollHistoryResponse(BaseResponse):
	response: Optional["GetLongPollHistoryResponseModel"] = None


class GetLongPollServerResponse(BaseResponse):
	response: Optional["GetLongPollServerResponseModel"] = None


class IsMessagesFromGroupAllowedResponse(BaseResponse):
	response: Optional["IsMessagesFromGroupAllowedResponseModel"] = None


class JoinChatByInviteLinkResponse(BaseResponse):
	response: Optional["JoinChatByInviteLinkResponseModel"] = None


class MarkAsImportantResponse(BaseResponse):
	response: Optional["MarkAsImportantResponseModel"] = None


class PinResponse(BaseResponse):
	response: Optional["PinResponseModel"] = None


class SearchConversationsExtendedResponse(BaseResponse):
	response: Optional["SearchConversationsExtendedResponseModel"] = None


class SearchConversationsResponse(BaseResponse):
	response: Optional["SearchConversationsResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
	response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


class SendResponse(BaseResponse):
	response: Optional["SendResponseModel"] = None


class SendUserIdsResponse(BaseResponse):
	response: Optional["SendUserIdsResponseModel"] = None


class SetChatPhotoResponse(BaseResponse):
	response: Optional["SetChatPhotoResponseModel"] = None


CreateChatResponseModel = int


class DeleteChatPhotoResponseModel(BaseResponse):
	message_id: Optional["integer"] = None
	chat: Optional["messageschat"] = None


class DeleteConversationResponseModel(BaseResponse):
	last_deleted_id: Optional["integer"] = None


DeleteResponseModel = typing.Dict[str, int]


EditResponseModel = Optional[Baseboolint]


class GetByConversationMessageIdResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetByIdExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetByIdResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetChatPreviewResponseModel(BaseResponse):
	preview: Optional["messageschatpreview"] = None
	profiles: Optional["array"] = None


GetChatChatIdsFieldsResponseModel = List[MessagesChatFull]


GetChatChatIdsResponseModel = List[MessagesChat]


GetChatFieldsResponseModel = Optional[Messageschatfull]


GetChatResponseModel = Optional[Messageschat]


class GetConversationMembersResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	chat_restrictions: Optional["messageschatrestrictions"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetConversationsByIdExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetConversationsByIdResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetConversationsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	unread_count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class GetHistoryAttachmentsResponseModel(BaseResponse):
	items: Optional["array"] = None
	next_from: Optional["string"] = None


class GetHistoryExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None
	conversations: Optional["array"] = None


class GetHistoryResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class GetImportantMessagesExtendedResponseModel(BaseResponse):
	messages: Optional["messagesmessagesarray"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None
	conversations: Optional["array"] = None


class GetImportantMessagesResponseModel(BaseResponse):
	messages: Optional["messagesmessagesarray"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None
	conversations: Optional["array"] = None


class GetIntentUsersResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None


class GetInviteLinkResponseModel(BaseResponse):
	link: Optional["string"] = None


GetLastActivityResponseModel = Optional[Messageslastactivity]


class GetLongPollHistoryResponseModel(BaseResponse):
	history: Optional["array"] = None
	messages: Optional["messageslongpollmessages"] = None
	credentials: Optional["messageslongpollparams"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None
	chats: Optional["array"] = None
	new_pts: Optional["integer"] = None
	from_pts: Optional["integer"] = None
	more: Optional["boolean"] = None
	conversations: Optional["array"] = None


GetLongPollServerResponseModel = Optional[Messageslongpollparams]


class IsMessagesFromGroupAllowedResponseModel(BaseResponse):
	is_allowed: Optional["baseboolint"] = None


class JoinChatByInviteLinkResponseModel(BaseResponse):
	chat_id: Optional["integer"] = None


MarkAsImportantResponseModel = List[int]


PinResponseModel = Optional[Messagespinnedmessage]


class SearchConversationsExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None


class SearchConversationsResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


class SearchExtendedResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None
	profiles: Optional["array"] = None
	groups: Optional["array"] = None
	conversations: Optional["array"] = None


class SearchResponseModel(BaseResponse):
	count: Optional["integer"] = None
	items: Optional["array"] = None


SendResponseModel = int


SendUserIdsResponseModel = List[Object]


class SetChatPhotoResponseModel(BaseResponse):
	message_id: Optional["integer"] = None
	chat: Optional["messageschat"] = None

CreateChatResponse.update_forward_refs()
DeleteChatPhotoResponse.update_forward_refs()
DeleteConversationResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
EditResponse.update_forward_refs()
GetByConversationMessageIdResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetChatPreviewResponse.update_forward_refs()
GetChatChatIdsFieldsResponse.update_forward_refs()
GetChatChatIdsResponse.update_forward_refs()
GetChatFieldsResponse.update_forward_refs()
GetChatResponse.update_forward_refs()
GetConversationMembersResponse.update_forward_refs()
GetConversationsByIdExtendedResponse.update_forward_refs()
GetConversationsByIdResponse.update_forward_refs()
GetConversationsResponse.update_forward_refs()
GetHistoryAttachmentsResponse.update_forward_refs()
GetHistoryExtendedResponse.update_forward_refs()
GetHistoryResponse.update_forward_refs()
GetImportantMessagesExtendedResponse.update_forward_refs()
GetImportantMessagesResponse.update_forward_refs()
GetIntentUsersResponse.update_forward_refs()
GetInviteLinkResponse.update_forward_refs()
GetLastActivityResponse.update_forward_refs()
GetLongPollHistoryResponse.update_forward_refs()
GetLongPollServerResponse.update_forward_refs()
IsMessagesFromGroupAllowedResponse.update_forward_refs()
JoinChatByInviteLinkResponse.update_forward_refs()
MarkAsImportantResponse.update_forward_refs()
PinResponse.update_forward_refs()
SearchConversationsExtendedResponse.update_forward_refs()
SearchConversationsResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()
SendResponse.update_forward_refs()
SendUserIdsResponse.update_forward_refs()
SetChatPhotoResponse.update_forward_refs()