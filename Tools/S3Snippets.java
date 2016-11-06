

public final my_bucket = "generationu-userfiles-mobilehub-762974824'";

public  void ReadAllSeniorFiles()
{
	//substitute for credentials
	BasicAWSCredentials creds = new BasicAWSCredientials("access_key", "secret_key");
	AmazonS3Client s3 =  new AmazonS3Client( creds,);
	
	//loop through objects in SeniorProfiles/
	GetObjectRequest Request;
	S3Object object;
	InputStream objectData;
	for( S3ObjectSummary summary : S3Objects.withPrefix(s3, my_bucket, "SeniorProfiles/") ) {
		
		//creates a new request for each object
		Request = new GetObjectRequest( summary.getBucketName(), summary.getKey());
		
		//get the object from the database
		 object = s3.getObject( Request);
		 
		 //Read the object's data into an InputStream
		 objectData = object.getObjectContent();
		 
		 //Load Senior data from xml
		 //insert your method here
	}

}
