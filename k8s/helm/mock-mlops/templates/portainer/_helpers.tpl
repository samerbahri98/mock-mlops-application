{{- define "portainer-hostname" -}}
{{- $environment := default "production" .Values.ingress.environment -}}
{{- $hostname := default "cluster.local" .Values.ingress.hostname -}}
{{- $branch := default "main" .Values.ingress.branch -}}
{{- if eq $environment "production" }}
{{- printf "%s.%s" "portainer" $hostname }}
{{- else if eq $environment "testing" }}
{{- printf "%s.%s" "portainer.test" $hostname }}
{{- else -}}
{{- printf "%s.%s.%s" "portainer" $branch $hostname }}
{{- end }}
{{- end }}
