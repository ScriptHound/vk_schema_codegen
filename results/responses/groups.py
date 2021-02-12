

class AddAddressResponse(BaseResponse):
	

class AddCallbackServerResponse(BaseResponse):
	server_id = None

class AddLinkResponse(BaseResponse):
	

class CreateResponse(BaseResponse):
	

class EditAddressResponse(BaseResponse):
	

class GetAddressesResponse(BaseResponse):
	count = None
	items = None

class GetBannedResponse(BaseResponse):
	count = None
	items = None

class GetByIdLegacyResponse(BaseResponse):
	

class GetByIdResponse(BaseResponse):
	groups = None
	profiles = None

class GetCallbackConfirmationCodeResponse(BaseResponse):
	code = None

class GetCallbackServersResponse(BaseResponse):
	count = None
	items = None

class GetCallbackSettingsResponse(BaseResponse):
	

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

class GetLongPollServerResponse(BaseResponse):
	

class GetLongPollSettingsResponse(BaseResponse):
	

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

class GetTagListResponse(BaseResponse):
	

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

class IsMemberResponse(BaseResponse):
	

class IsMemberUserIdsExtendedResponse(BaseResponse):
	

class IsMemberUserIdsResponse(BaseResponse):
	

class SearchResponse(BaseResponse):
	count = None
	items = None