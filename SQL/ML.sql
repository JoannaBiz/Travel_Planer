--sp_configure 'external scripts enabled', 1;
--RECONFIGURE;

EXECUTE sp_execute_external_script
	@language = N'Python',
	@script = N'
import pkg_resources
import pandas as pd
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key,i.version)for i in installed_packages])
df = pd.DataFrame(installed_packages_list, columns=["PackageName", "PackageVersion"])
OutputDataSet = df
'  
WITH RESULT SETS((PackageName nvarchar(150), PackageVersion nvarchar(150)))
