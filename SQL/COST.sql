/* To prevent any potential data loss issues, you should review this script in detail before running it outside the context of the database designer.*/
BEGIN TRANSACTION
SET QUOTED_IDENTIFIER ON
SET ARITHABORT ON
SET NUMERIC_ROUNDABORT OFF
SET CONCAT_NULL_YIELDS_NULL ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
COMMIT
BEGIN TRANSACTION
GO
CREATE TABLE dbo.COST
	(
	ID int NOT NULL,
	Category varchar(MAX) NOT NULL,
	Name_Cost nvarchar(MAX) NOT NULL,
	Plan_Cost money NOT NULL,
	Real_cost money NULL,
	Paid bit NULL,
	Date datetime2(7) NULL,
	Who_paid nvarchar(50) NULL,
	Who_need_return_money nvarchar(50) NULL,
	Is_returned nvarchar(50) NULL
	)  ON [PRIMARY]
	 TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE dbo.COST ADD CONSTRAINT
	PK_COST PRIMARY KEY CLUSTERED 
	(
	ID
	) WITH( STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

GO
ALTER TABLE dbo.COST SET (LOCK_ESCALATION = TABLE)
GO
COMMIT

--INSERT INTO dbo.COST (ID,Category,Name_Cost,Plan_Cost)
--values(1,'Transport','Bilety lotnicze',5000);