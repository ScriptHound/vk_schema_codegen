


class AddAddressResponse(BaseResponse):
	response = None


class AddCallbackServerResponse(BaseResponse):
	response = None


class AddLinkResponse(BaseResponse):
	response = None


class CreateResponse(BaseResponse):
	response = None


class EditAddressResponse(BaseResponse):
	response = None


class GetAddressesResponse(BaseResponse):
	response = None


class GetBannedResponse(BaseResponse):
	response = None


class GetByIdLegacyResponse(BaseResponse):
	response = None


class GetByIdResponse(BaseResponse):
	response = None


class GetCallbackConfirmationCodeResponse(BaseResponse):
	response = None


class GetCallbackServersResponse(BaseResponse):
	response = None


class GetCallbackSettingsResponse(BaseResponse):
	response = None


class GetCatalogInfoExtendedResponse(BaseResponse):
	response = None


class GetCatalogInfoResponse(BaseResponse):
	response = None


class GetCatalogResponse(BaseResponse):
	response = None


class GetInvitedUsersResponse(BaseResponse):
	response = None


class GetInvitesExtendedResponse(BaseResponse):
	response = None


class GetInvitesResponse(BaseResponse):
	response = None


class GetLongPollServerResponse(BaseResponse):
	response = None


class GetLongPollSettingsResponse(BaseResponse):
	response = None


class GetMembersFieldsResponse(BaseResponse):
	response = None


class GetMembersFilterResponse(BaseResponse):
	response = None


class GetMembersResponse(BaseResponse):
	response = None


class GetRequestsFieldsResponse(BaseResponse):
	response = None


class GetRequestsResponse(BaseResponse):
	response = None


class GetSettingsResponse(BaseResponse):
	response = None


class GetTagListResponse(BaseResponse):
	response = None


class GetTokenPermissionsResponse(BaseResponse):
	response = None


class GetExtendedResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class IsMemberExtendedResponse(BaseResponse):
	response = None


class IsMemberResponse(BaseResponse):
	response = None


class IsMemberUserIdsExtendedResponse(BaseResponse):
	response = None


class IsMemberUserIdsResponse(BaseResponse):
	response = None


class SearchResponse(BaseResponse):
	response = None


AddAddressResponseModel = None


class AddCallbackServerResponse(BaseResponse):
	server_id = None


AddLinkResponseModel = None


CreateResponseModel = None


EditAddressResponseModel = None


class GetAddressesResponse(BaseResponse):
	count = None
	items = None


class GetBannedResponse(BaseResponse):
	count = None
	items = None


GetByIdLegacyResponseModel = array


class GetByIdResponse(BaseResponse):
	groups = None
	profiles = None


class GetCallbackConfirmationCodeResponse(BaseResponse):
	code = None


class GetCallbackServersResponse(BaseResponse):
	count = None
	items = None


GetCallbackSettingsResponseModel = None


class GetCatalogInfoExtendedResponse(BaseResponse):
	enabled = None
	categories = None


class GetCatalogInfoResponse(BaseResponse):
	enabled = None
	categories = None


class GetCatalogResponse(BaseResponse):
	count = None
	items = None


class GetInvitedUsersResponse(BaseResponse):
	count = None
	items = None


class GetInvitesExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None
	groups = None


class GetInvitesResponse(BaseResponse):
	count = None
	items = None


GetLongPollServerResponseModel = None


GetLongPollSettingsResponseModel = None


class GetMembersFieldsResponse(BaseResponse):
	count = None
	items = None


class GetMembersFilterResponse(BaseResponse):
	count = None
	items = None


class GetMembersResponse(BaseResponse):
	count = None
	items = None


class GetRequestsFieldsResponse(BaseResponse):
	count = None
	items = None


class GetRequestsResponse(BaseResponse):
	count = None
	items = None


class GetSettingsResponse(BaseResponse):
	access = None
	address = None
	audio = None
	articles = None
	recognize_photo = None
	city_id = None
	contacts = None
	links = None
	sections_list = None
	main_section = None
	secondary_section = None
	age_limits = None
	country_id = None
	description = None
	docs = None
	events = None
	obscene_filter = None
	obscene_stopwords = None
	obscene_words = None
	event_group_id = None
	photos = None
	public_category = None
	public_category_list = None
	public_date = None
	public_date_label = None
	public_subcategory = None
	rss = None
	start_date = None
	finish_date = None
	subject = None
	subject_list = None
	suggested_privacy = None
	title = None
	topics = None
	twitter = None
	video = None
	wall = None
	website = None
	phone = None
	email = None
	wiki = None


GetTagListResponseModel = array


class GetTokenPermissionsResponse(BaseResponse):
	mask = None
	permissions = None


class GetExtendedResponse(BaseResponse):
	count = None
	items = None


class GetResponse(BaseResponse):
	count = None
	items = None


class IsMemberExtendedResponse(BaseResponse):
	member = None
	invitation = None
	can_invite = None
	can_recall = None
	request = None


IsMemberResponseModel = None


IsMemberUserIdsExtendedResponseModel = array


IsMemberUserIdsResponseModel = array


class SearchResponse(BaseResponse):
	count = None
	items = None