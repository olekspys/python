import os

def extract_lines(file_line_pairs):
    results = []
    for file_line in file_line_pairs:
        print(f"Processing input: {file_line}")  # Debug log
        try:
            # Split the input into file path and line number
            file_path, line_number = file_line.rsplit(':', 1)  # Use rsplit for correct parsing
            line_number = int(line_number)  # Convert line number to integer

            # Check if the file exists
            if not os.path.isfile(file_path):
                results.append(f"{file_path}:{line_number}: [ERROR] File not found")
                continue

            # Read the specified line
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Check if the line number is within the file's line count
            if line_number < 1 or line_number > len(lines):
                results.append(f"{file_path}:{line_number}: [ERROR] Line number out of range")
                continue

            # Get the line content and strip any trailing whitespace
            line_content = lines[line_number - 1].strip()
            results.append(f"{file_path}:{line_number}:{line_content}")

        except ValueError:
            results.append(f"{file_line}: [ERROR] Invalid input format (expected format: 'file_path:line_number')")
        except Exception as e:
            results.append(f"{file_path}:{line_number}: [ERROR] {str(e)}")
    
    return results

# Example usage
if __name__ == "__main__":
    input_data = [
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/cache/IEntity.java:20",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/core/atrails/IAuditTrailsService.java:21",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/core/DiffTagCommentHistoryOwner.java:28",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/core/ICommentable.java:17",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/core/ICommentLine.java:17",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/core/IHistoryRecord.java:18",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/core/IIdentifiable.java:20",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/core/IPathReview.java:20",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/security/IUserRepo.java:21",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/setup/AbstractDoctor.java:20",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/business/setup/IDoctor.java:21",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IAuxNumberService.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/ICallHistoryRepo.java:9",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/ICannedMessageRepo.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IDiagCodeRepo.java:25",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IEntryRepo.java:26",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IHisIndexRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IHisSpecimenRepo.java:24",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IInsuranceRepo.java:24",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IMiscInformationRepo.java:27",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IMpisRepo.java:19",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IOrderRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IPatientRepo.java:20",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IRecurTestRepo.java:26",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IReportRepo.java:26",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/ISpecimenRepo.java:25",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IStayRepo.java:21",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/ITestDiagRepo.java:24",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/ITestHistoryItemRepo.java:25",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/core/IRepo.java:24",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/secuirty/IRestrictionItemRepo.java:24",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/secuirty/ISecuritySystemDao.java:19",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IAuxDoctorRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IClinicRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ICsfPrintersRepo.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IDepartmentRepo.java:8",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IDiagnosisRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IDoctorRepo.java:25",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IDrugRepo.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IEnvironmentRepo.java:9",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IInsuranceDefinitionRepo.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IKeypadRepo.java:26",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ILabDoctorRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ILocationRepo.java:24",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IMicroMediaDefinitionRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IMicroWorklistRepo.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IMmtTrackingLocationRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IMmtTrackingStatusRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IOLCCRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IOrganismRepo.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IPanelRepo.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IPatternRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IRegionRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IReportSetupRepo.java:25",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ISiteRepo.java:19",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ISourceRepo.java:25",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ISpecimenDefinitionRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ISpecimenQualityRepo.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ITagDefinitionRepo.java:23",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ITemperatureRepo.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ITestDefinitionFinder.java:26",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/ITestDefinitionRepo.java:25",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IUniversalIDRepo.java:22",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/repo/setup/IWorkstationRepo.java:9",
        "D:/SVN/lws/branches/lws_4_5_8_P/java/lmc-business/src/com/softcomputer/softlab/utils/AgeUtils.java:24"
    ]

    output = extract_lines(input_data)
    for line in output:
        print(line)






