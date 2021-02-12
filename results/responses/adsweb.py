

class GetAdCategoriesResponse(BaseResponse):
	categories = None

class GetAdUnitCodeResponse(BaseResponse):
	html = None

class GetAdUnitsResponse(BaseResponse):
	count = None
	ad_units = None

class GetFraudHistoryResponse(BaseResponse):
	count = None
	entries = None

class GetSitesResponse(BaseResponse):
	count = None
	sites = None

class GetStatisticsResponse(BaseResponse):
	next_page_id = None
	items = None