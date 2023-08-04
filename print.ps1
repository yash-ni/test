$directory = "logs"

Get-ChildItem -Path $directory | ForEach-Object {
    if ($_.PSIsContainer -eq $false) {
        Write-Host ""
        Write-Host "Contents of $($_.Name):"
        Get-Content $_.FullName
        Write-Host ""
    }
}