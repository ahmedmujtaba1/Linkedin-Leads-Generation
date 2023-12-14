let targets = [
    "www.linkedin.com/sales-api/salesApiProfiles",
    "www.linkedin.com/sales/profile/",
    "www.linkedin.com/connected/api/v1/contacts",
	"www.linkedin.com/sales-api/salesApiPeopleSearch",
	"www.linkedin.com/sales-api/salesApiLeadSearch",
    "www.linkedin.com/connected/api/v2/contacts",
    "www.linkedin.com/sales-api/salesApiMessagingThreads",
    "www.linkedin.com/communities-api/v1/memberships/community",
    "www.linkedin.com/sales/search/results",
    "www.linkedin.com/voyager/api/",
    "www.linkedin.com/recruiter/api/smartsearch",
    "www.linkedin.com/sales-api/salesApiMailbox"
];

try {
    let OldFetch = window.fetch;
    window.fetch = function () {
        return new Promise((resolve, reject) => {
            OldFetch.apply(this, arguments).then(async (response) => {
                if (response.ok) {
                    let res = response.clone();
                    res.text().then(t => handleRequests(res, t)).catch(e => { });
                }
                resolve(response);
            }).catch((error) => reject())
        });
    }
} catch (error) {

}
async function handleRequests(response, res) {
    var resp = {};
    try {
        resp.data = res;
        resp.type = response.type;
        resp.url = response.url;
        if (typeof resp.url != "undefined" && targets.filter(target => resp.url.indexOf(target) > -1).length > 0) {
            
            if(
				resp.url.indexOf('salesApiPeopleSearch') !== -1 ||
				resp.url.indexOf('salesApiLeadSearch') !== -1
			){

				jsonProfiles = JSON.parse(resp.data);

				console.log(jsonProfiles)

				///
					allProfiles = {};

					if(jsonProfiles['elements'] !== undefined){

						// $.each(jsonProfiles['elements'], function( k, v ) {

						jsonProfiles['elements'].forEach(function(v) {

							// console.log(v);

							userObject = {};
							userObject['company_size'] = '';
							userObject['domain'] = '';
							userObject['founded'] = '';
							userObject['industry'] = '';
							userObject['job_title'] = '';
							userObject['linkedin_id'] = '';
							userObject['past_company'] = '';
							userObject['rewards'] = '';
							userObject['skills'] = '';
							userObject['type'] = '';
							userObject['user__summary__experience'] = '';
							userObject['user_city'] = '';
							userObject['user_company_id'] = '';
							userObject['user_company_name'] = '';
							userObject['user_first_name'] = '';
							userObject['user_keywords'] = '';
							userObject['user_last_name'] = '';
							userObject['user_number_connections'] = '';
							userObject['user_other_email'] = '';
							userObject['user_profile_picture'] = '';
							userObject['user_source'] = 'linkedin';
							userObject['user_summary'] = '';
							userObject['user_url'] = '';
							userObject['vcard'] = '';
							userObject['website'] = '';

							if(v['currentPositions'] !== undefined && v['currentPositions']['companyName'] !== undefined){
								userObject['user_company_name'] = InterceptorcleanCompanyName(v['currentPositions']['companyName']);
							}

							if(v['currentPositions'] !== undefined && v['currentPositions']['companyUrn'] !== undefined){
								userObject['user_company_id'] = InterceptorextractIdNewLinkedinCompany(v['currentPositions']['companyUrn']);
							}

							if(v['geoRegion'] !== undefined && v['geoRegion'] !== undefined){
								userObject['user_city'] = v['geoRegion'];
							}

							if(v['currentPositions'] !== undefined && v['currentPositions']['title'] !== undefined){
								userObject['job_title'] = InterceptorUnescapeHtml(v['currentPositions']['title']);
							}

							if(v['firstName'] !== undefined){
								userObject['user_first_name'] = InterceptorcleanNameComma(v['firstName']);
							}

							if(v['lastName'] !== undefined){
								userObject['user_last_name'] = InterceptorcleanNameComma(v['lastName']);
							}

							if(v['objectUrn'] !== undefined){
								userObject['linkedin_id'] = InterceptorextractIdNewLinkedin(v['objectUrn']);
							}
							
							if(v['currentPositions'] !== undefined && v['currentPositions']['companyName'] !== undefined){
								companyNameSearch = v['currentPositions']['companyName'];
							}else {
								companyNameSearch = '';
							}

							if(v['currentPositions'] !== undefined && v['currentPositions'].length > 0){


												for (var index = 0; index < v['currentPositions'].length; index++) {
													var element = v['currentPositions'][index];

													if(element['current'] !== undefined && element['current'] === true){

														if(element['title'] !== undefined){

															userObject['job_title'] = InterceptorUnescapeHtml(element['title']);
														

														}

														if(element['companyName'] !== undefined){

															userObject['user_company_name'] = InterceptorcleanCompanyName(element['companyName']);
															companyNameSearch = element['companyName'];

														}

														if(element['companyUrn'] !== undefined){

															userObject['user_company_id'] = InterceptorextractIdNewLinkedinCompany(element['companyUrn']);

														}

													}
													
												}

							}

							if(v['entityUrn'] !== undefined){
								userObject['user_url'] = v['entityUrn'].toString().replace('urn:li:fs_salesProfile:(', 'https://www.linkedin.com/sales/people/')
								userObject['user_url'] = userObject['user_url'].replace(',ibn_)', '');
								userObject['user_url'] = userObject['user_url'].replace(')', '');

							}

							if(userObject['linkedin_id'] !== ''){
								allProfiles[userObject['linkedin_id']] = userObject;
							}

							console.log(userObject);

						});



						localStorage.setItem("INTERCEPTOR3837383", JSON.stringify(allProfiles));



					}
				
				///


            }
            
            let resevent = new CustomEvent("datachannel", {
                detail: resp
            });
            //document.dispatchEvent(resevent)
        }
    } catch (e) { }
}



String.prototype.InterceptorReplaceAllX = function(search, replacement) {
	var target = this;
	return target.replace(new RegExp(search, 'g'), replacement);
	};
	
	
	
	
	
	
	
	function isNumeric(num){
	return !isNaN(num)
	}
	
	function InterceptorcleanName(string){
	
		string2 = string.InterceptorReplaceAllX('- ', '').toString();
	
		string3 = string2.toString().replace('.', '');
		string3 = string3.toString().replace('. ', '');
	
		words_name = string3.split(" ");
	
		names__array = [];
	
		names__array.push(words_name[0]);
	
		if(words_name[2] != undefined && words_name[3] != undefined){
		names__array.push(words_name[1]+"-"+words_name[2]+"-"+words_name[3]);
		}else if(words_name[2] != undefined) {
		names__array.push(words_name[1]+"-"+words_name[2]);
		}else {
		names__array.push(words_name[1]);       
		}
	
		return names__array;
	
	}
	
	function InterceptorcleanCompanyName(string){
		
			string = string.replace(', Inc.', '')
			string = string.replace(' Inc.', '')
			string = string.replace(' Inc', '')
			string = string.replace(' LLC', '')
			string = string.replace(', LLC', '')
			string = string.trim();
			string = string.replace('<b>', '');
			string = string.replace('</b>', '');
		
			string = string.replace('&lt;b&gt;', '');
			string = string.replace('&lt;/b&gt;', '');
	
			string = string.replace(', INC.', '');
	
			return string;
	
	}
	
	function InterceptorCompanyPremium(string){
	
		companyName = '';
	
		if(string.indexOf('at ') !== -1){
		string = string.split('at ');
		companyName = string[1];
		}
	
		if(string.indexOf('chez ') !== -1){
		string = string.split('chez ');
		companyName = string[1];
		}
	
		if(string.indexOf('en ') !== -1){
		string = string.split('en ');
		companyName = string[1];
		}
	
		if(companyName.indexOf('- ') !== -1){
		companyName = companyName.split('- ');
		companyName = companyName[0];
		}
	
		if(companyName.indexOf('| ') !== -1){
		companyName = companyName.split('| ');
		companyName = companyName[0];
		}
	
		companyName = companyName.trim();
	
		return companyName;
	
	}
	
	function InterceptorextractIdNewLinkedinCompany(str){
	
		extract_id = str.replace("urn:li:fs_salesCompany:", "");
	
		return extract_id;
	
	}
	
	function InterceptorextractIdNewLinkedin(str){
	
		extract_id = str.replace("urn:li:member:", "");
	
		return extract_id;
	
	}
	
	function InterceptorUnescapeHtml(safe) {
	
	var tmp = document.createElement("DIV");
	tmp.innerHTML = safe;
	vrs =  tmp.textContent || tmp.innerText || "";
	vrs = vrs.replace(/<(?:.|\n)*?>/gm, '')
	return vrs;
	}
	
	
	function InterceptorcleanNameComma(string){
	
		if(string === undefined){
		return '';
		}
	
		if(string.indexOf(',') > -1){
	
		string = string.split(',');
		string = string[0]
	
	}
	
	return string;
	
	}
	