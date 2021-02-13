


class GetCatalogResponse(BaseResponse):
	response = None


class GetFriendsListResponse(BaseResponse):
	response = None


class GetLeaderboardExtendedResponse(BaseResponse):
	response = None


class GetLeaderboardResponse(BaseResponse):
	response = None


class GetMiniAppPoliciesResponse(BaseResponse):
	response = None


class GetScopesResponse(BaseResponse):
	response = None


class GetScoreResponse(BaseResponse):
	response = None


class GetResponse(BaseResponse):
	response = None


class ImageUploadResponse(BaseResponse):
	response = None


class SendRequestResponse(BaseResponse):
	response = None


class GetCatalogResponse(BaseResponse):
	count = None
	items = None
	profiles = None


class GetFriendsListResponse(BaseResponse):
	count = None
	items = None


class GetLeaderboardExtendedResponse(BaseResponse):
	count = None
	items = None
	profiles = None


class GetLeaderboardResponse(BaseResponse):
	count = None
	items = None


class GetMiniAppPoliciesResponse(BaseResponse):
	privacy_policy = None
	terms = None


class GetScopesResponse(BaseResponse):
	count = None
	items = None


GetScoreResponseModel = None


class GetResponse(BaseResponse):
	count = None
	items = None


class ImageUploadResponse(BaseResponse):
	hash = None
	image = None


SendRequestResponseModel = None